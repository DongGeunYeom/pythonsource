import re

pattern = re.compile("D?A")

print("? : 최소 0 ~ 최대 1")
print(pattern.search("A"))
print(pattern.search("DA"))
print(pattern.search("AA"))


print()
pattern = re.compile("D*A")
print("* : 최소 0 ~ 최대 무한대")
print(pattern.search("A"))
print(pattern.search("DA"))
print(pattern.search("DDDDDDDDDDDDDDDDDDDDA"))

print()
pattern = re.compile("D+A")
print("+ : 최소 1 ~ 최대 무한대")
print(pattern.search("A"))  # None
print(pattern.search("DA"))
print(pattern.search("DDDDDDDDDDDDDDDDDDDDA"))

print()
pattern = re.compile("AD{2}A")
print(" {n}: n 만큼 반복")
print(pattern.search("ADA"))  # None
print(pattern.search("ADDA"))
print(pattern.search("ADDDDDDDDDDDDDDDDDDDDA"))  # None

print()
pattern = re.compile("AD{2,6}A")
print(" {n, m}: 최소 n, 최대 m 만큼 반복")
print(pattern.search("ADA"))  # None
print(pattern.search("ADDA"))
print(pattern.search("ADDDDDDDDDDDDDDDDDDDDA"))  # None
