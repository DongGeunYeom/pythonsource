# https://news.nate.com/rank/interest=sc_ent 랭킹 뉴스 추출
# 제목, 기사 제공자(연합뉴스...) 1 ~ 50위
import re
import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook

res = requests.get("https://news.nate.com/rank/interest?sc=ent")
soup = BeautifulSoup(res.text, "lxml")

pattern = re.compile("[0-9]{4}-[0-9]{2}-[0-9]{2}")

# top5_list
top5_list = soup.select("div.mduSubjectList > div")
for idx, news in enumerate(top5_list, 1):
    # 타이틀
    title = news.select_one("a strong").get_text()
    # 신문사(신문사 날짜) - 한글, 영문문자만
    media = news.select_one("span.medium").get_text()
    print(f"{idx} : {title} - {media}")
    print(pattern.search(media))

# top50_list
top50_list = soup.select("#postRankSubject li")

for idx, news in enumerate(top50_list, 6):
    # 타이틀
    title = news.select_one("a").get_text()
    # 신문사
    media = news.select_one("span.medium").get_text()
    print(f"{idx} : {title} - {media}")


# # 순위 가져오기
# number5 = soup.select("div.mduSubjectList > dl > dt:nth-child(1) > em:nth-child(1)")

# number50 = soup.select("ul.mduSubject > li > dl > dt:nth-child(1) > em:nth-child(1)")

# # for number in number5:
# #     print(number.get_text())

# for number in number50:
#     print(number.get_text())


# # 제목 가져오기
# title5 = soup.select(
#     "div.mduSubjectList > div:nth-child(2) > a:nth-child(1) > span:nth-child(2) > strong:nth-child(1)"
# )

# title50 = soup.select("ul.mduSubject > li > a")

# # for title in title5:
# #     print(title.get_text())

# # for title in title50:
# #     print(title.get_text())

# # 기사 작성자 가져오기
# provider5 = soup.select("div.mduSubjectList > div:nth-child(2) > span:nth-child(2)")

# provider50 = soup.select("ul.mduSubject> li > span:nth-child(3)")

# # for provider in provider5:
# #     print(provider.get_text()[:-10])

# # for provider in provider50:
# #     print(provider.get_text())
