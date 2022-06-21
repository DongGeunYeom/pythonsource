import re

pattern = re.compile("[abcdefgABCDEFG]")
print("[] : 괄호 안에 들어가는 문자가 들어 있는 패턴")
print(pattern.search("abc123"))  # <re.Match object; span=(0, 1), match='a'>
print(pattern.search("DEG456"))  # <re.Match object; span=(0, 1), match='D'>

print()
pattern = re.compile("[a-gA-G]")
print("[ - ] : 패턴을 범위로 처리 ")
print(pattern.search("abc123"))  # <re.Match object; span=(0, 1), match='a'>
print(pattern.search("DEG456"))

print()
pattern = re.compile("[a-zA-Z]+")
print("[a-zA-Z]+ : 알파벳 전체를 패턴으로 처리")
print(pattern.search("abc123"))  # <re.Match object; span=(0, 3), match='abc'>
print(pattern.search("DEG456"))  # <re.Match object; span=(0, 3), match='DEG'>

print()
pattern = re.compile("[^a-zA-Z0-9]")
print("[^a-zA-Z0-9] : 대괄호 안의 '^' 는 포함하지 않는")
print(pattern.search("abc123"))  # None
print(pattern.search("#%&G456"))  # <re.Match object; span=(0, 1), match='#'>


print()
pattern = re.compile("[가-힣]")
print("[가-힣] : 한글 찾기")
print(pattern.search("abc123"))  # None
print(pattern.search("가나다라"))  # <re.Match object; span=(0, 1), match='가'>
