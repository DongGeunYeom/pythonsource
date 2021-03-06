# naver open api 이용하기 - 도서검색
# 도서명, link, 출판사
import requests
from openpyxl import Workbook
from datetime import datetime

# 엑셀 파일 생성
wb = Workbook()

# 기본 시트 활성화
ws = wb.active
ws.title = "도서1000"

# A 컬럼 width 조절
ws.column_dimensions["B"].width = 60
ws.column_dimensions["C"].width = 80
ws.column_dimensions["D"].width = 15

ws.append(["순위", "상품명", "상품URL", "출판사", "출판일"])

client_id = "Hj3r1GGUiiu9JIwInsa3"
client_secret = "ZIX8dh0JJT"

url = "https://openapi.naver.com/v1/search/shop.json"

headers = {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret}

# 주소 생성
# url = "https://openapi.naver.com/v1/search/shop.json?query=a&display=100&start=101"
# url = "https://openapi.naver.com/v1/search/shop.json?query=a&display=100&start=201"
# url = "https://openapi.naver.com/v1/search/shop.json?query=a&display=100&start=301"
# url = "https://openapi.naver.com/v1/search/shop.json?query=a&display=100&start=401"
num = 0
start = 1
for idx in range(10):
    start_num = start + (idx * 100)

    url = (
        "https://openapi.naver.com/v1/search/book.json?query=베르나르&display=100&start="
        + str(start_num)
    )

    res = requests.get(url, headers=headers)
    # json 데이터 확인
    # print(res.json())
    for item in res.json()["items"]:
        num += 1
        print(num, item["title"], item["link"], item["publisher"], item["pubdate"])
        ws.append(
            [num, item["title"], item["link"], item["publisher"], item["pubdate"]]
        )


# 파일명 : clien_220620.xlsx
today = datetime.now().strftime("%y%m%d")
filename = f"naverbook_{today}.xlsx"
# 엑셀 저장
wb.save("./rpabasic/crawl/download/" + filename)
