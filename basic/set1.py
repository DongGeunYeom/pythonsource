# set : 집합
# 자바 Set 과 같은 개념
# 중복 허용 안됨
# 순서 없음

set1 = set()
set2 = set("hello") # l 하나 제거되고 순서 바뀜 
set3 = set([1,2,3,4])
set4 = set([1,2,3,4,6,6]) # 6 하나 제거됨
set5 = set({"no":"1", "name":"hong","age":24}) # key값만 순서가 바뀐 뒤 출력

print(set1) # set()
print(set2)
print(set3)
print(set4)
print(set5)

print()


# set ==> tuple 변환
print(tuple(set3))

# set ==> list 변환
print(list(set3))

# set은 교집합, 합집합, 차집합에 유용함
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print("s1, s2 교집합", s1 & s2)
print("s1, s2 교집합", s1.intersection(s2))

print("s1, s2 합집합", s1 | s2)
print("s1, s2 합집합", s1.union(s2))

print("s1, s2 차집합", s1 - s2)
print("s1, s2 차집합", s1.difference(s2))

# 함수
# add() : 값 하나 추가
s1.add(70)
print(s1)

# update() : 여러 개의 값을 한꺼번에 추가
s1.update([18,19,20])
print(s1)

# remove() : 특정 값 제거
s1.remove(2)
print(s1)