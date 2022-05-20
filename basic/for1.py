# for
# for 변수 in 범위

# range(시작값, 마지막 범위, 증감)
print(range(5))  # range(0, 5)
print(list(range(5)))  # [0, 1, 2, 3, 4]
print(list(range(1, 5)))  # [1, 2, 3, 4]
print(list(range(0, 10, 2)))  # [0, 2, 4, 6, 8]
print(list(range(50, 1, -2)))

# 0 ~ 9 출력
for i in range(10):
    print(i, end=" ")

print()
for i in range(1, 11):
    print(i, end=" ")

print()
for i in range(1, 101, 2):
    print(i, end=" ")

print()
sum2 = 0
for i in range(1, 101):
    sum2 += i
print(sum)

# 실습 : 사용자에게 숫자 입력받음 1~입력값 합계 구한후 출력
# num1 = int(input("숫자를 입력해주세요."))
# sum1 = 0
# for i in range (1, num1+1):
#     sum1 += i
# print(sum1)

# print("1 ~ {} 까지 합 : {}".format(num1, sum(range(1, num1+1))))


# 문자열 출력
word = "dreams"
for s in word:
    print(s)

# 이중 for 문
for i in range(3):
    for j in range(3):
        print(j, end=" ")
    print()

# 구구단 2~9단
# for i in range(2, 10):
#     for j in range(1, 10):
#         print("{} * {} = {}".format(i, j, (i*j)), end="\t")
#     print()

# break, continue
i = 1
while i <= 10:
    if i == 5:
        break
    print(i, end=" ")
    i += 1

print()
i = 1
while i <= 10:
    i += 1
    if i % 2 == 1:
        continue
    print(i, end=" ")

print()
i = 0
# 실습 1~10 출력, i가 5인 경우는 출력하지 않음
while i <= 9:
    i += 1
    if i == 5:
        continue
    print(i, end=" ")

print()
# for +  continue
for i in range(1, 11):
    if i == 5:
        continue
    print(i, end=" ")
