# 피보나치 수열

# 바로 앞의 두 수를 더한 값을 다음 값으로 추가
# 0, 1, 1, 2, 3, 5, 8, 13, 21

def fib(n):
    if n <= 1 :
        return n
    else:
        return fib(n-2) + fib(n-1)

if __name__ == "__main__":
    print(fib(2)) # 0번 값 + 1번 값
    print(fib(3)) # 1번 값 + 2번 값
    print(fib(7)) # 5번 값 + 6번 값