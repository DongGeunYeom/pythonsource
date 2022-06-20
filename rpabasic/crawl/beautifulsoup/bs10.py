import requests
from bs4 import BeautifulSoup

res = requests.get("https://pythonscraping.com/pages/page3.html")
soup = BeautifulSoup(res.text, "lxml")

# h1 태그 가져오기
h1 = soup.select_one("h1")
print(h1)

# 상단 내용 가져오기
content = soup.select_one("div#content")
print(content.get_text())

# 모든 img 태그 가져오기
img_all = soup.select("img")  # soup.find_all("img")
print(img_all)

# 타이틀 행 가져오기
# giftList > tbody:nth-child(1) > tr:nth-child(1) > th:nth-child(i)
title = soup.select("table#giftList > tr:nth-child(1)")
print(title)
for item in title:
    print(item.get_text())

# 테이블 내용 가져오기
table = soup.find("table", id="giftList")
print(table.get_text())

# 가격만 가져오기
# for i in range(1, 6):
#     price = soup.select("#gift" + str(i) + "> td:nth-child(3)")
#     for item in price:
#         print(item.get_text())

cost_list = soup.select("tr.gift")
for cost in cost_list:
    # print(cost)
    print(cost.find_all("td")[2].get_text())
