# requests + beautifulsoup4
# 객체생성(페이지소스, 파서)
import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.v.daum.net/v/20220613070010390")
# print(res.text)

# parser : html.parser( 기본 - 설치가 필요 없음 )
# soup = BeautifulSoup(res.text, "html.parser")
soup = BeautifulSoup(res.text, "lxml")

# print(soup) # 일반출력
# print(soup.prettify())  # 들여쓰기

# <head> 태그 안 내용 가져오기
# print(soup.head)

# <body> 태그 가져오기
# print(soup.body)

# <title> 태그 가져오기
# print(soup.title) # 타이틀 태그 전체
# print(soup.title.name) # 태그명 가져오기
# print(soup.title.get_text()) # 태그 안 텍스트 가져오기
# print(soup.title.string) # 태그 안 텍스트 가져오기

# 기사 제목 가져오기
title = soup.select_one("h3.tit_view")
print("기사 제목 : " + title.get_text())

# 기사 작성 날짜와 시간 가져오기
time = soup.select_one("span.num_date")
print("기사 날짜 : " + time.get_text())

# 기사 작성자 가져오기
writer = soup.select_one("span.txt_info")
print("기사 작성자 : " + writer.get_text())

# 기사 첫 번째 문단 가져오기
first_text = soup.select_one("p")
print("기사 첫 번째 문단 : " + first_text.get_text())

print()
contents = soup.select("p")
print(contents)
for para1 in contents:
    print(para1.get_text())
