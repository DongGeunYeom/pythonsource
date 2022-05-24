# list 자료형 (배열과 같은 개념)
# 다양한 형태의 자료들을 담을 수 있음

# 생성
list1 = []
list2 = list(["a", "b", "c"])  # 굳이 이렇게 안 해도 됨
list3 = ["a", "b", "c", 1, 2]
list4 = [1, 2, 3, 4, 5, 6.5]
list5 = [
    1,
    2,
    ["Life", "is", "short"],
]  # 여기서 -1이라 하면 오른쪽 끝부터라 배열 묶음인  ["Life", "is", "short"] 이거 자체가 -1에 해당
list6 = list()

# print(list1)
# print(list2)
# print(list3)
# print(list4)
# print(list5)
# print(list6)


# 인덱싱 -> -1 은 오른쪽 끝
# print("llist2[0]", list2[0])
# print("list3[-1]", list3[-1])
# print("list4[3]", list4[3])
# print("list4[3] + list5[1]", (list4[3] + list5[1]))
print("list5[2][0]", list5[2][0])
print("list5[-1][2]", list5[-1][2])


# 슬라이싱(어디부터 어디까지 자르기)
print("llist2[0:3]", list2[0:3])
print("list3[1:3]", list3[1:3])
print("list5[2:]", list5[2:])
print("list5[2][0]", list5[2][0])


list6 = [1, 2, ["a", "b", ["Life", "is"]]]  # 3차원

# is 출력
print("list6[2][2][1] = ", list6[2][2][1])
print("list6[-1][-1][1] = ", list6[-1][-1][1])
print("list6[2][-1][-1] = ", list6[2][-1][-1])


# 연산자
# + => 연결 : 리스트들을 연결시켜준다 앞에서부터 차례대로, 자료형과 상관없이 리스트끼리의 연결은 가능, 리스트의 인덱스로 값과 값 연결에서는 자료형이 다르면 에러
# 인덱싱에서 + 는 산술연산자 의미
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = ["a", "b", "c"]

print("list1 + list2 = ", (list1 + list2))
print("list1 + list3 = ", (list1 + list3))
print("list1[0] + list2[1] = ", (list1[0] + list2[1]))
# print("list1[0] + list3[1] = ", (list1[0] + list3[1]))

print()

# * => 반복
print("list1 * 3 = ", (list1 * 3))
print("list1[0] * 3 = ", (list1[0] * 3))  # 값을 꺼내서 곱하는건 산술연산자


print()
# 리스트 요소 값 변경
print("list1 = ", list1)
list1[1] = 7
print("list1 = ", list1)
list1[2] = "Life"
print("list1 = ", list1)  # 바로 위에서 7로 바꿔서 바꾼 값으로 유지


print()
print("list2 = ", list2)
list2[1:2] = [10, 11]  # 지정한 위치에 기존값 밀어내기
print("list2 = ", list2)
list2[1] = [15, 16, 17]  # 범위가 아닌 위치로 지정하여 값을 넣는다면 그 값 대신에 리스트로 들어간다
print("list2 = ", list2)


print()
# 리스트 요소 삭제
print("list1 = ", list1)
# del list1[2]
# del list1[1:3]
list1[1:3] = []
print("list1 = ", list1)


print()

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
# for문을 활용하여 리스트 값을 출력할 수도 있다
for num in list1:
    print(num, end=" ")


print()

numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
# 리스트 안의 숫자 중 100 이상인 숫자 출력
for num in numbers:
    if num >= 100:
        print(num)

# 리스트 안의 숫자가 홀수/짝수인지 판별하기
for num in numbers:
    if num % 2 == 0:
        print("{}는 짝수 : ".format(num))
    else:
        print("{}는 홀수 : ".format(num))

# 리스트 안의 숫자들의 자릿수 출력하기
# 273은 3자리, 103은 3자리, 5는 1자리 ...
for num in numbers:
    print("{} 는 {} 자리 수".format(num, len(str(num))))

print()
# 함수
# append() : 리스트에 요소 추가
list1 = [1, 2, 3]
list1.append(4)  # 요소 하나만 추가하기, 기존 리스트에 리스트로 넣는게 아니라 값만 넣기
list1.append([5, 6, 7])  # 리스트 구조로 추가하면 기존 리스트 안에 리스트가 생기는 구조가 됨
print(list1)

print()

# 1~100 까지의 숫자 중에서 짝수 리스트 생성
even = []
for num in range(1, 101):
    if num % 2 == 0:
        even.append(num)

print(even)

print()


# sort : 기본적으로 오름차순 정렬
list1 = [1, 4, 3, 2]
print("정렬 전 ", list1)
list1.sort()
print("정렬 후 ", list1)

print()

list2 = ["k", "z", "a", "b", "r"]
print("정렬 전 ", list2)
list2.sort(reverse=True)  # 내림차순 정렬
print("정렬 후 ", list2)

print()

list3 = ["k", "z", "K", "b", "A"]
print("정렬 전 ", list3)
list3.sort()
print("정렬 후 ", list3)

print()

list4 = ["ㄷ", "ㄱ", "ㄴ", "ㅁ", "ㅅ"]
print("정렬 전 ", list4)
list4.sort()
print("정렬 후 ", list4)

print()

# reverse() : 리스트 뒤집기(정렬이 아니라 그냥 리스트 순서를 뒤에서부터 거꾸로 출력해주는 것 뿐)
list1 = ["a", "c", "b", "z"]
list1.reverse()
print("list1", list1)


print()

# sort() + reverse() => 내림차순
list1 = [3, 12, 1, 5, 9, 2, 7]
print("정렬 전 ", list1)
list1.sort()
list1.reverse()
print("정렬 후 ", list1)

print()

# index() : 위치반환
print("list1", list1)
print("list1 에 9가 있는지 확인", list1.index(9))
# 못 찾으면 ValueError 발생
# print("list1 에 45가 있는지 확인", list1.index(45)) # => 그래서 얘는 에러남

print()
# insert(삽입위치, 삽입할 요소)
list1 = [1, 2, 3]
list1.insert(0, 4)
print("list1 요소 삽입 후 : ", list1)

print()

# remove(제거할 요소)
list1.remove(2)
print("list1 요소 제거 후 : ", list1)

print()

# pop() : 리스트 요소 맨 마지막 요소 끄집어 내기
# pop(위치) : 해당 위치 요소 끄집어 내기
list1 = [1, 2, 3, 4, 5, 6, 7]
print("list1", list1)
list1.pop()
print("list1 pop() 후 : ", list1)
list1.pop(2)
print("list1 pop(2) 후 : ", list1)

print()

# count(x) : 리스트에 포함된 요소 x 의 개수 세기
print("list1.count(2) : ", list1.count(2))  # list1 에 2가 몇 개 있어 라는 의미

print()

# extend(x 리스트) : 원래 리스트에 x 리스트 더하기
list2 = [16, 17, 18]
print("list1 + list2 = ", (list1 + list2))
list1.extend(list2)
print("list1 extend : ", list1)

print()
# clear() : 요소 모두 삭제(비우기)
list1.clear()
print("list1 clear() 후 : ", list1)

print()

# 요소 in 리스트명 : 리스트 안에 해당 요소가 있느냐(True/False)
fruits = ["딸기", "바나나", "수박", "사과", "참외"]
print("딸기" in fruits)
print("두리안" in fruits)

print()

# 리스트가 비어 있으면 거짓
list1 = []
if list1:
    print("참")
else:
    print("거짓")

# enumerate() : 하나씩 가지고 나올 수 있는 자료형 에 사용 가능

# 리스트 요소 출력
for num in enumerate(numbers):
    print(num)  # (0, 273) : (인덱스, 값) => 튜플 자료형 형태로 반환

print()

for idx, num in enumerate(numbers, start=1):
    print(idx, num)

print()

# 실습
# A 학급엥 총 10명의 학생이 있다. 이 학생들의 충간고사 점수는 다음과 같다
# 70,66,55,75,90,95,80,100,87
# 중간고사 점수를 리스트로 생성하고 A학급의 평균을 구하시오
jumsu = [70, 66, 55, 75, 90, 95, 80, 100, 87]
total = 0
for num in jumsu:
    total = total + num

print("A 학급 평균 : %.2f" % (total / len(jumsu)))

# for 사용 안 하고 애초에 존재하는 sum() 함수 이용하기
print("A 학급 평균 : %.2f" % (sum(jumsu) / len(jumsu)))

print()

# 다음 리스트에서 Apple 항목만 삭제하고 출력하기
# ["Banana","Apple","Orange","Grape"]
fruits = ["Banana", "Apple", "Orange", "Grape"]
fruits.remove("Apple")  # == del fruits[1]
print(fruits)

