import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

res = requests.get("https://ko.wikipedia.org/wiki/%ED%81%B0%EA%B9%8C%EB%A7%88%EA%B7%80")

soup = BeautifulSoup(res.text, "lxml")
# print(soup.prettify())

# 사진저장
# .infobox > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > a:nth-child(1) > img:nth-child(1)
image1 = soup.select_one(
    ".infobox > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > a:nth-child(1) > img:nth-child(1)"
)
print(image1)
print(image1["src"])

image2 = soup.select_one(
    "div.thumb:nth-child(8) > div:nth-child(1) > a:nth-child(1) > img:nth-child(1)"
)


# 이미지 다운로드 - urlretrieve
path = "./rpabasic/crawl/download/"
# urlretrieve("이미지 원본 경로", "다운로드 받을 경로")
# urlretrieve("http:" + image1["src"], path + "bird1.jpg")
urlretrieve("http:" + image2["src"], path + "bird2.jpg")
