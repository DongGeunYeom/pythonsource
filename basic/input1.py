# 입력 : input()

# msg = input()
# print(msg)

# msg = input("이름 입력: ")
# print(msg)

# num1 = int(input("Num1 : ")) # str 타입 입력
# num2 = int(input("Num2 : "))
# print(num1+num2)

# 실습 
# 년 / 월 / 일 형태로 입력받은 후 10년 후 날짜를 출력하기
# 2022 / 05 / 20 => 2032년 05월 20일

# year = int(input("년을 입력해주세요."))
# month = int(input("월을 입력해주세요."))
# day = int(input("일을 입력해주세요."))

# print(("{0}년 {1}월 {2}일".format(year+10,month,day)))

date1 = input("날짜입력(년/월/일)")
# pos = date1.find("/")
# year = int(date1[:pos]) + 10
# print("입력한 날짜의 10년 후는? %s "% (str(year)+"년 "+date1[5:7]+"월 "+date1[8:]+"일"))

date1 = date1.split("/") # ['2022', '05', '20]
print("입력한 날짜의 10년 후는? %s "% (str(int(date1[0])+10)+"년 "+date1[1]+"월 "+date1[2]+"일"))
