import re

pattern = re.compile("[a-z]+")  # 소문자(최소 1 ~ 최대 무한대)

matched = pattern.match("Dave")
print("match()", matched)  # match() None
print()
searched = pattern.search("Dave")
print("search()", searched)  # search() <re.Match object; span=(1, 4), match='ave'>

# re.sub(패턴, 바꿀 문자열, 원본 문자열) : 찾아서 바꾸기
ori_text = "DDA D1A DDDA DA"
print(re.sub("D.A", "Dave", ori_text))  # Dave Dave DDave DA

print()

# findall() : 정규식과 일치하는 모든 문자열을 찾아 리스트로 반환
print("findall() 후")
print(pattern.findall("Game of Life in Python"))
pattern = re.compile("[a-zA-Z]+")
print(pattern.findall("Game of Life in Python"))

print()

# finditer() : 정규식과 일치하는 모든 문자열을 찾아 iterator 객체로 반환
for m in pattern.finditer("Game of Life in Python"):
    print(m.group())

# split() : 정규식을 기준으로 문자열을 분리한 후 리스트로 반환
pattern = re.compile(":")
print(pattern.split("python:java"))
