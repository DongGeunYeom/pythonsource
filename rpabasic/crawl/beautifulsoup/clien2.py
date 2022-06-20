# clien 팁과 강좌 게시판 크롤링
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from datetime import datetime

res = requests.get("https://www.clien.net/service/board/lecture")
soup = BeautifulSoup(res.text, "lxml")

# 게시판 제목 가져오기

title_list = soup.select("a.list_subject > span.subject_fixed")
# for title in title_list:
#     print(title.get_text().strip())

# 1~ 5 page
# https://www.clien.net/service/board/lecture?&od=T31&category=0&po=1
# https://www.clien.net/service/board/lecture?&od=T31&category=0&po=4

# 엑셀
# 엑셀 파일 생성
wb = Workbook()

# 기본 시트 활성화
ws = wb.active

# A 컬럼 width 조절
ws.column_dimensions["A"].width = 80
ws.column_dimensions["B"].width = 15

# 시트명 새로 지정
ws.title = "팁과강좌"

# 제목행 지정
ws.append(["글제목", "작성날짜"])


for page_num in range(5):  # 0~4
    if page_num == 0:  # 1page
        res = requests.get("https://www.clien.net/service/board/lecture")
    else:
        res = requests.get(
            "https://www.clien.net/service/board/lecture?&od=T31&category=0&po="
            + str(page_num)
        )

    soup = BeautifulSoup(res.text, "lxml")
    title_list = soup.select("a.list_subject > span.subject_fixed")

    # 날짜/시간 가져오기
    time_list = soup.find_all("span", class_="timestamp")
    date_list = soup.select(
        "div.list_content > div.list_item > div.list_time > span > span"
    )

    for idx, title in enumerate(title_list):
        print(title.get_text().strip(), date_list[idx].get_text()[:10])
        ws.append([title.get_text().strip(), date_list[idx].get_text()[:10]])
    print("*" * 80)

# 파일명 : clien_220620.xlsx
today = datetime.now().strftime("%y%m%d")
filename = f"clien_{today}.xlsx"
# 엑셀 저장
wb.save("./rpabasic/crawl/download/" + filename)
