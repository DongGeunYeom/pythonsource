# 사용자가 정의한 모듈 실습

# import prints

# prints.prt1()
# prints.prt2()


# from prints import prt1

# prt1()


# import mod1

# print(mod1.safe_sum(15, 25))
# print(mod1.safe_sum(15, "25"))


# from mod1 import sum

# print(sum(45, 25))


# import calc

from calc import FourCal

num1, num2 = 10, 5
# four1 = calc.FourCal(num1, num2)

four1 = FourCal(num1, num2)
print("{} + {} = {}".format(num1, num2, four1.add()))
print("{} - {} = {}".format(num1, num2, four1.sub()))
print("{} * {} = {}".format(num1, num2, four1.mul()))
print("{} / {} = {}".format(num1, num2, four1.div()))
