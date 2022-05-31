# 재귀호출 : 함수 안에서 자기 자신을 부르는 것

# 잘못된 예제
# def hello():
#     print("hello")
#     hello()

# hello() # maximum recursion depth exceeded while calling a Python object

def fact(n):
    # 기본단계 - 끝내는 부분
    if n == 1:
        return 1
    # 반복단계
    else: 
        return n * fact(n-1)

if __name__ == "__main__":
    print(fact(3))
    print(fact(5))
    print(fact(10))