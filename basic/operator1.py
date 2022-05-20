# 연산자
# 산술연산자 : +, -, *, /(실수), //(정수), %, **

a, b = 5, 3
print(a+b, a-b, a*b, a/b, a//b, a%b, a**b)

print()
s1, s2, s3 = "100", "100.123", "9999999"
print(s1+s2+s3) # + : 연결 => 100100.1239999999
print(float(s1)+float(s2)+float(s3))
# print(s1+1)     # TypeError: can only concatenate str (not "int") to str
print(int(s1)+1) 

# 복합대입연산자 : +=, -=, /=, //=, %=, **=
a = 10
a += 5
print("a",a)
a == 5
print("a",a)
a *= 5
print("a",a)
a /= 5
print("a",a)
a //= 5
print("a",a)
a %= 5
print("a",a)
a **= 5
print("a",a)

print()
# 실습 : 777,777원
# 화폐교환 : 5만원권/1만원권/5천원권/1천원권

a = 777777

m50 = a//50000
a %= 50000

m10 =  a//10000
a %= 10000

m5 = a//5000
a %= 5000 

m1 = a//1000
a %= 1000

print("50,000원 : %d 장" % m50)
print("10,000원 : %d 장" % m10)
print("5,000원 : %d 장" % m5)
print("1,000원 : %d 장" % m1)
print("나머지 돈 : %d" % a)

# 관계연산자 : ==, !=, >, <, >=, <=
a, b = 10,0
print(a==b, a!=b, a>b, a<b, a>=b, a<=b)

# 논리연산자 : and, or, not
print(100 > 60 and 60 > 15)
# print(100 > 60 && 60 > 15)
print(100 > 60 or 60 > 15)
print(not 60 < 15)
print(not False)
print(not True)
# print(!True)

# 비트연산자
print(10 & 7)
print(10 | 7)
print((100 > 60) & (60 > 15))
