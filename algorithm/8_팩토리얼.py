# 팩토리얼 구하기 - for
# 문제 : 1부터 n까지의 곱
# 입력 : 1 ~ n
# 출력 : 1 ~ n 까지의 곱 4! = 4 * 3 * 2 * 1

def fact(number):
    result = 1
    for i in range(1, number+1):
        result *= i 

    return result

if __name__ == "__main__":
    print(fact(3))
    print(fact(5))
    print(fact(10))