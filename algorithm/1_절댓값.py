# 절댓값

# a의 절댓값 구하기
# 1) 부호 판단
import math


def abs_sign(a):
    if a >= 0 :
        return a
    else:
        return -a

# 2) 제곱 후 제곱근 
def abs_sign2(a):
    b = a*a
    return math.sqrt(b)


if __name__ == "__main__":
    print("절댓값", abs_sign(5))
    print("절댓값", abs_sign(-3))
    print
    print("절댓값", abs_sign2(5))
    print("절댓값", abs_sign2(-3))