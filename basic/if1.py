# 파이썬 {} 사용하지 않음 / 들여쓰기 사용함
# if
# if True :
#     print("True")

a = 200
# if a <100 :
#     print("a는 100보다 작다")

# print("조건문에서 들여쓰기는 중요함")

# a는 100과 200사이에 있다
# if a >= 100 and a <=200:
#     print("a는 100과 200사이에 있다")

# if 100 <= a <= 200:
#     print("a는 100과 200사이에 있다")

# 실습
a, b, c = 12, 6, 18

# 가장 큰 수 출력하기
# max = a
# if max < b:
#     max = b
# if max < c:
#     max = c
# print("제일 큰 수",max)

# if ~ else
if True:
    print("True")
else:
    print("False")

a = 55
if a < 100:
    print("a는 100보다 작다")
else:
    print("a는 100보다 크다")

print()
score, grade = 90, "A"
if score >= 90 and grade == "A":
    print("합격")
else:
    print("불합격")

# number = int(input("숫자를 입력해주세요."))
# if number % 2 == 0:
#     print("짝수입니다.")
# else:
#     print("홀수입니다.")

from calendar import day_abbr
import datetime

now = datetime.datetime.now()
print(now)  # 2022-05-20 15:11:20.906823
print(
    "{}년 {}월 {}일 {}시 {}분 {}초".format(
        now.year, now.month, now.day, now.hour, now.minute, now.second
    )
)

if now.hour >= 12:
    print("오후입니다.")
else:
    print("오전입니다.")

print("오전" if now.hour < 12 else "오후")

# 삼항 연산자
str = "안녕하세요" if True else "반갑습니다."
print(str)

# 중첩 if
a = 75
if a > 50:
    if a < 100:
        print("a는 50보다 크고 100보다 작다.")
    else:
        print("a는 50보다 크고 100보다 크거나 같다")
else:
    print("50보다 작거나 같다")

# 다중 if : if ~ elif ~ else
num = 90
if num >= 90:
    print("등급 A", num)
elif num >= 80:
    print("등급 B", num)
elif num >= 70:
    print("등급 C", num)
elif num >= 60:
    print("등급 D", num)
else:
    print("등급 E", num)

print()
age, height = 27, 180

if age >= 20:
    if height >= 170:
        print("A 지망 가능")
    elif height >= 160:
        print("B 지망 가능")
    else:
        print("지원 불가")
else:
    print("20세 이상 지원 가능")

# 실습
# 사용자에게 점수를 입력 받고 학점 출력
# > 80 A, > 60 B, > 40 C, >20 D, E

num = int(input("점수 입력"))

if num > 80:
    print("등급 A", num)
elif num > 60:
    print("등급 B", num)
elif num > 40:
    print("등급 C", num)
elif num > 20:
    print("등급 D", num)
else:
    print("등급 E", num)

# 사칙계산기
# 사용자에게 숫자 2개와 연산자(+, -, *, /, %, //, **) 입력 받은 후 연산 후 결과 출력

address = input("숫자 2개와 연산자를 입력해주세요. 각 값은 띄어쓰기 해주세요.")
value = address.split(" ")
num1, num2 = int(value[0]), int(value[1])
oper = value[2]


if oper == "+":
    print("결과 값 : ", num1 + num2)
elif oper == "-":
    print("결과 값 : ", num1 - num2)
elif oper == "*":
    print("결과 값 : ", num1 * num2)
elif oper == "/":
    print("결과 값 : ", num1 / num2)
elif oper == "%":
    print("결과 값 : ", num1 % num2)
elif oper == "//":
    print("결과 값 : ", num1 // num2)
elif oper == "**":
    print("결과 값 : ", num1**num2)
else:
    print("연산자 확인")
