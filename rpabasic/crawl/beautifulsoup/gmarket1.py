import requests
from bs4 import BeautifulSoup

url = "https://www.gmarket.co.kr/"

res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")

# 1차 카테고리 추출하기

first_category = soup.find_all("a", class_="link__1depth-item", limit=9)

for idx in first_category:
    print("1차 카테고리명 : " + idx.get_text())

print("------------------------")
# 2차 카테고리 추출하기
second_category = soup.find_all("li", class_="list-item__2depth", limit=69)
print(second_category)
for idx in second_category:
    # print("2차 카테고리명 : " + idx.get_text())
    print(idx.string)

# for depth in second_category:
#     href = depth.find("a")["href"]
#     print(depth.get_text(), href)

# get_text() : 태그(자식태그 포함)가 가지고 있는 모든 문자열 가져오기
# string : 태그가 가지고 있는 문자열만 가져오기
