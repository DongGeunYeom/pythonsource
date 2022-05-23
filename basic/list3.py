# List Comprehension

# 리스트 생성 1 ~ 100 
# numbers = []
# for n in range(1, 101):
#     numbers.append(n)

# print(numbers)

# numbers = list(range(1, 101))
# print(numbers)

# numbers2 =[n for n in range(1, 101)]
# print(numbers2)

# list1 = ["갑","을","병","정"]
# for n in list1:
#     if n != "정":
#         print(n, end=" ")

# print()
# print([n for n in list1 if n != "정"])

# 1 ~ 100 숫자 중에서 홀수만 출력
list1 = [n for n in range(1,101) if n % 2 == 1]
print(list1)

# 5글자 이상의 단어만 출력
list2 = ["nice","study","python","anaconda","abe"]
print([n for n in list2 if len(n) >= 5])

# 소문자만 출력
list3 = ["A", "b", "C", "D", "e", "z", "a"]
print([n for n in list3 if n.islower()])

# 아래 리스트를 각 요소에 2배 한 후 출력
list4 = [1,2,3,4]
print([n * 2 for n in list4])
print([n * 2 for n in range(5)])
print([n * n for n in range(5)])