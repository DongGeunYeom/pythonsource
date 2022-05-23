# list 자료형(배열과 같은 개념)
# 다양한 형태의 자료들을 담을 수 있음

# 생성
from traceback import print_tb


list1 = []
list2 = list(["a", "b", "c"])
list3 = ["a", "b", "c", 1, 2]
list4 = [1, 2, 3, 4, 5, 6.5]
list5 = [1, 2, ["Life", "is", "short"]]
list6 = list()

print(list1)
print(list2)
print(list3)
print(list4)
print(list5)
print(list6)

list6 = [1, 2, ["a", "b", ["Life", "is"]]]
print(list6)
# is 출력
print(list6[-1][-1][-1])

# 연산자 
# + 
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = ['a', 'b', 'c']

print("list1 + list2 = ", (list1+list2))
print("list1 + list3 = ", (list1+list3))
print("list1[0] + list2[1] = ", (list1[0]+list2[1])) 
# print("list1[0] + list3[1] = ", (list1[0]+list3[1])) # TypeError: unsupported operand type(s) for +: 'int' and 'str'

print()
# *
print("list1 * 3 = ", (list1*3))
print("list1[0] * 3 = ", (list1[0]*3))

print()
# 리스트 요소 값 변경
print("list1 = ", list1)
list1[1] = 7
print("list1 = ",list1)
list1[2] = "Life"
print("list1 = ",list1)

print()

print("list2 = ",list2)
list2[1:2] = [10, 11]
print("list2 = ", list2)
list2[1] = [15,16,17]
print("list2 = ",list2)
print()

# 리스트 요소 삭제
print("list1 = ", list1)
#del list1[2]

list1[1:3] = []
#del list1[1:3]

print("list1 = ",list1)
print()
list1 = [1,2,3,4,5,6,7,8]
for num in list1:
    print(num, end=" ")

print()
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
# 리스트 안의 숫자 중 100 이상인 숫자만 출력
for num2 in numbers:
    if num2 >= 100:
        print(num2, end=" ")

print()
# 리스트 안의 숫자가 홀수/짝수인지 판별하기

for num2 in numbers:
    if num2 % 2 == 0:
        print(num2,"는 짝수입니다")
    else:
        print(num2,"는 홀수입니다.")


print()
# 리스트 안의 숫자들의 자릿수 출력하기
# 273은 3자리, 103은 3자리, 5는 1자리
for num2 in numbers:
     print("{}은 {}자리".format(num2, len(str(num2))))

print()
# 함수
# append()
list1 = [1, 2, 3]
list1.append(4)
list1.append([4, 5, 6])
print(list1)

# 1~100까지의 숫자 중에서 짝수 리스트 생성
even = []
i = 0
for i in range(1, 101):
    if i % 2 == 0:
        even.append(i)
print(even)

# sort : 정렬 : 오름차순 정렬(기본), sort(reverse=True): 내림차순
list1 = [1,4,3,2,5]
print("정렬 전",list1)
list1.sort()
print("정렬 후",list1)

list2 = ["k","z", "a", "c", "r"]
print("정렬 전",list2)
list2.sort(reverse=True) # 내림차순 정렬
print("정렬 후",list2)

# A : 65, a : 97
list3 = ["K","z", "A", "c", "r"]
print("정렬 전",list3)
list3.sort()
print("정렬 후",list3)

list4 = ["ㄷ", "ㄱ", "ㄴ", "ㅎ", "ㅈ"]
print("정렬 전",list4)
list4.sort()
print("정렬 후",list4)

# reverse() : 리스트 뒤집기 
list1 = ["a", "c", "b", "z"]
list1.reverse()
print("list1",list1)

# sort() + reverse() : 내림차순 정렬
list1 = [3, 17, 1, 5, 9, 2, 7]
print("정렬 전 ", list1)
list1.sort()
list1.reverse()
print("정렬 후", list1)
print()

# index(): 위치 반환
print("list1", list1)
print("list1 에 9가 있는지 확인", list1.index(9)) 
# print("list1 에 45가 있는지 확인", list1.index(45)) # ValueError: 45 is not in list
print()

# insert(삽입위치, 삽입할 요소)
list1 = [1, 2, 3]
list1.insert(0, 4)
print("list1 요소 삽입 후", list1)

print()
# remove(제거할 요소) : 첫 번째로 나오는 요소 삭제
list1.remove(2)
print("list1 요소 제거 후", list1)

print()
# pop() : 리스트 맨 마지막 요소 끄집어 내기
# pop(위치) : 해당 위치 요소 끄집어 내기
list1 = [1,2,3,4,5,6,7]
print("list1",list1)
list1.pop()
print("list1 pop() 후",list1)
list1.pop(2)
print("list1 pop(2) 후",list1)

print()
# conut(x) : 리스트에 포함된 요소 x의 개수 세기
print("list1.count(2)",list1.count(2))

print()
# extend(x 리스트) : 원래 리스트에 x 리스트 더하기 
list2 = [16,17,18]
print("list1 + list2 = ", (list1+list2))
list1.extend(list2)
print("list1 extend ",list1)

print()
# clear() : 요소 모두 삭제
list1.clear()
print("list1 clear() 후", list1)

print()
# 요소 in 리스트명 : 리스트 안에 해당 요소가 있는지 확인(True or False)
fruits = ["딸기", "바나나", "수박", "사과", "참외"]
print("딸기" in fruits) # boolean type 반환
print("두리안" in fruits)

# 리스트가 비어 있으면 거짓
list1 = []
if list1:
    print("참")
else:
    print("거짓")

# 리스트 요소 출력
for num in enumerate(numbers):
    print(num) # (0, 273) : (인덱스, 값) => 튜플 자료형 형태로 반환

print()
# enumerate : 하나씩 가지고 나올 수 있는 자료형에 사용 가능
# idx, num = (0, 283)
for idx,num in enumerate(numbers, start=1):
    print(idx, num)

# 실습
# A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
# 70, 66, 55, 75, 90, 95, 80, 85, 100, 87
# 중간고사 점수를 리스트로 생성하고 A 학급의 평균을 구하시오

A = [70, 66, 55, 75, 90, 95, 80, 85, 100, 87]
sum1 = 0
for i in A:
    sum1 += i
print("A 학급의 평균 = %.2f" % (sum1/len(A)))

print("A 학급의 평균 : %.2f" % (sum(A)/len(A)))

# 다음 리스트에서 Apple 항목만 삭제하고 추력하기
# ["Banana", "Apple", "Orange", "Grape"]
fruits =  ["Banana", "Apple", "Orange", "Grape"]
fruits.remove("Apple") # del fruits[1]
print("Apple 삭제 후 ", fruits)

print()

