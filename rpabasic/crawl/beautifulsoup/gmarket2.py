# gmarket best - 컴퓨터/전자 항목 추출
import requests
from bs4 import BeautifulSoup

url = "http://corners.gmarket.co.kr/Bestsellers?viewType=G&groupCode=G06"

res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")

# 1차 카테고리 추출하기
test1 = soup.select("div.best-list li")

for idx, item in enumerate(test1, 1):

    # 상품명
    name = item.select_one("a.itemname")
    name2 = name.get_text().lstrip("[").split("]").pop()

    # 가격
    price = item.select_one("div.s-price strong span").get_text()

    # name["href"]를 이용해서 requests.get() 요청
    product_url = name["href"]
    res = requests.get(product_url)
    detail_soup = BeautifulSoup(res.text, "lxml")

    # 회사명 추출(회사명 없으면 셀러명 추출)
    company = detail_soup.select_one("span.text__brand > span.text")

    if not company:
        company = detail_soup.select_one("span.text__seller > a")
    # AttributeError: 'NoneType' object has no attribute 'get_text'

    # 순위, 상품명, 가격, 회사명, 상품상세정보 url
    print(
        f"{idx} : {name2} - {price} / 회사명 : {company.get_text()} / 상세정보 : {product_url}"
    )
