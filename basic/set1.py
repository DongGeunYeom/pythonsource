# set : 집합
# 자바 Set 과 같은 개념
# 중복 허용 안됨
# 순서 없음 - 인덱싱, 슬라이싱 사용할 수 없음

set1 = set()
set2 = set("Hello")
set3 = set([1, 2, 3, 4])
set4 = set([1, 2, 3, 4, 6, 6])
set5 = set({"no": "1", "name": "hong", "age": 24})

print(set1)  # set()
print(set2)  # {'H', 'e', 'o', 'l'}
print(set3)
print(set4)
print(set5)  # {'age', 'no', 'name'}


print()

# set ==> tuple 변환
print(tuple(set3))

# set ==> list 변환
print(list(set3))


# 교집합, 합집합, 차집합 구하기

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print("s1,s2 교집합", s1 & s2)
print("s1,s2 교집합", s1.intersection(s2))

print()

print("s1,s2 합집합", s1 | s2)
print("s1,s2 합집합", s1.union(s2))

print()
print("s1,s2 차집합", s1 - s2)
print("s1,s2 차집합", s1.difference(s2))


# 함수
# add() : 값 하나 추가
print(s1)
s1.add(17)
print(s1)

# update() : 여러 개의 값을 한꺼번에 추가
s1.update([18, 19, 20])
print(s1)


# remove() : 특정 값 제거
s1.remove(2)
print(s1)
