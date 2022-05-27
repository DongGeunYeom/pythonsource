# dictionary(딕셔너리)
# 자바의 Map 과 같은 개념
# key, value를 한 쌍으로 갖는 자료형
# key 값을 이용해 value 찾아냄
# {key1:value1, key2:value2....}


# 생성 - key 값은 중복 불가
dict1 = {"name": "park", "age": 12}
dict2 = {0: "Hello Python", 1: "Hello coding"}
dict3 = {"arr": [0, 1, 2, 3, 4]}

print(dict1)
print(dict2)
print(dict3)

# 딕셔너리에서 원하는 값 가져오기
print(dict1["age"])
# print(dict1["addr"]) # KeyError: 'addr'

print()

# 딕셔너리에서 쌍 추가
dict1["birth"] = "1115"
print(dict1)

dict2[2] = ["Hello Java", "hello jsp"]
print(dict2)

dict3["rank"] = (16, 17, 18)
print(dict3)


print()
# 딕셔너리에서 쌍 삭제
del dict1["birth"]
print(dict1)

# 실습
# numbers 내부에 들어있는 숫자가 각각 몇 번 등장하는지를 딕셔너리로 작성하여 출력하기
numbers = [1, 2, 6, 8, 4, 3, 2, 1, 9, 5, 4, 9, 7, 2, 1, 3, 5, 4, 8, 9, 7, 2, 3]
counter = {}
# 출력
# {1:3, 2:4, 6:1, 8:2.....}

for num in numbers:
    counter[num] = numbers.count(num)

print(counter)

print()
# 딕셔너리 함수
# keys() : key 값을 모아서 보여줌
print(dict1.keys())  # dict_keys(['name', 'age'])
print(dict3.keys())

print(list(dict1.keys()))

# values() : value 값을 모아서 보여줌
print(dict1.values())
print(dict2.values())
print(dict3.values())

# itmes() : Key, Value 쌍 가져오기
print(dict1.items())
print(dict2.items())
print(dict3.items())

# get() : key로 value 가져오기
print(dict1["age"])
print(dict1.get("age"))
print(dict1.get("addr"))  # None

# in : 해당 key가 딕셔너리 안에 있는지 조사
print("name" in dict1)
print(4 in dict2)
print("rank" in dict3)


print()

my_info = {"name": "kim", "age": 30, "city": "seoul"}

for k in my_info.keys():
    print(k)

print()
for v in my_info.values():
    print(v)

print()
for k, v in my_info.items():
    print(k, v)


# 실습
# 딕셔너리 dict1을 아래와 같은 조건으로 생성하시오
# 'A':90, 'B':80, 'C':70
dict1 = {"A": 90, "B": 80, "C": 70}

# 작성된 dict1에서 B키에 해당하는 값만 출력
print(dict1["B"])
print(dict1.get("B"))

# B키 값을 삭제한 후 dict1 출력
del dict1["B"]
print(dict1)

# dict2 생성
# '성인':100000, '청소년':70000, '어린이':30000
dict2 = {"성인": 100000, "청소년": 70000, "어린이": 30000}

# dict2 항목에 소아:0 항목 추가 후 출력
dict2["소아"] = 0
print(dict2)

# key 값만 출력
print(dict2.keys())

# value 값만 출력
print(dict2.values())
