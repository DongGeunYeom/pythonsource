from bs4 import BeautifulSoup

# 문서 가져오기

with open("./rpabasic/crawl/beautifulsoup/story.html", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, "lxml")

# print(soup.prettify())

# 3. find~~

# 첫 번째 p 태그
# p1 = soup.p

p1 = soup.find("p")  # soup.find("p", class_="title")
print(p1)

# 형제 p 태그 찾기
p2 = soup.find("p", class_="story")
# print(f"p 두 번째 >> {p2}")
# print(f"p 두 번째 내용 >> {p2.get_text()}")
# print(f"p 두 번째 속성들 >> {p2.attrs}")
# print(f"p 두 번째 특정 속성 값 >> {p2['class']}")

# p3 = p2.next_sibling.next_sibling
p3 = p2.find_next_sibling("p")
# print(f"p 세 번째 >> {p3}")
# print(f"p 세 번째 내용 >> {p3.get_text()}")
# print(f"p 세 번째 속성들 >> {p3.attrs}")
# print(f"p 세 번째 특정 속성 값 >> {p3['class']}")

# 첫 번째 a
a1 = soup.find("a")

# 두 번째 a
a2 = soup.find("a", id="link2")

# print(f"a 두 번째 >> {a2}")
# print(f"a 두 번째 내용 >> {a2.get_text()}")
# print(f"a 두 번째 속성들 >> {a2.attrs}")
# print(f"a 두 번째 특정 속성 값 >> {a2['id']}")

# 세 번째 a
a3 = soup.find("a", id="link3")
a3 = soup.find("a", class_="sister", id="link3")
a3 = soup.find("a", attrs={"class": "sister", "id": "link3", "data-io": "tillie"})

# print(f"a 세 번째 >> {a3}")
# print(f"a 세 번째 내용 >> {a3.get_text()}")
# print(f"a 세 번째 속성들 >> {a3.attrs}")
# print(f"a 세 번째 특정 속성 값 >> {a3['id']}")

# find_all()

a = soup.find_all("a")
# print(a)
b = soup.find_all("b")
# print(b)

# limit : 개수 지정해서 가지고 오기
a = soup.find_all("a", limit=2)

a = soup.find_all("a", class_="sister")

# 텍스트 노드 값 이용해서 가져오기
a = soup.find_all(string=["Elsie"])
a = soup.find_all(string=["Elsie", "Lacie"])
print(a)
