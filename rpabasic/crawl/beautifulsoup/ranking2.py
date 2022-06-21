# https://news.nate.com/rank/interest=sc_ent 랭킹 뉴스 추출 + 엑셀저장(nate_오늘날짜.xlsx)
# 제목, 기사 제공자(연합뉴스...) 1 ~ 50위
import requests
import re
from bs4 import BeautifulSoup
from openpyxl import Workbook
from datetime import datetime

res = requests.get("https://news.nate.com/rank/interest?sc=ent")
soup = BeautifulSoup(res.text, "lxml")

# 엑셀
wb = Workbook()
ws = wb.active
ws.title = "연예랭킹뉴스"
ws.column_dimensions["A"].width = 5
ws.column_dimensions["B"].width = 80
ws.column_dimensions["C"].width = 15

# 제목행 지정
ws.append(["순위", "기사 제목", "기사 제공자"])

# 정규식
pattern = re.compile("[0-9]{4}-[0-9]{2}-[0-9]{2}")
pattern2 = re.compile("[가-힣a-zA-Z0-9{3}]+")

# top5_list
top5_list = soup.select("div.mduSubjectList > div")
for idx, news in enumerate(top5_list, 1):
    # 타이틀
    title = news.select_one("a strong").get_text()
    # 신문사(신문사날짜) - 한글, 영문문자만
    media_date = news.select_one("span.medium").get_text()

    # re.sub()
    pattern3 = re.compile("[\d-]+")
    media = re.sub(pattern3, "", media_date)
    print(f"{idx} : {title} - {media}")

    # split() ==> list ['마이데일리', '2022-06-21']
    # media = pattern3.split(media_date)

    # print(f"{idx} : {title} - {media[0]}")
    ws.append([idx, title, media])

# top50_list
top50_list = soup.select("#postRankSubject li")

for idx, news in enumerate(top50_list, 6):
    # 타이틀
    title = news.select_one("a").get_text()
    # 신문사
    media = news.select_one("span.medium").get_text()
    print(f"{idx} : {title} - {media}")
    ws.append([idx, title, media])


# 파일명 : clien_220620.xlsx
today = datetime.now().strftime("%y%m%d")
filename = f"nate_{today}.xlsx"
# 엑셀 저장
wb.save("./rpabasic/crawl/download/" + filename)
wb.close()
