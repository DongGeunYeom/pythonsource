# 최대공약수 구하기
# 두 개 이상의 정수의 공통 약수 중에서 가장 큰 값
# 알고리즘 : 두 수중 더 작은 값을 i에 저장
#            i가 두 수의 공통된 약수인지 확인
#            공통된 약수이면 이 값을 결과값으로 돌려주기
#            공통된 약수가 아니면 i를 1만큼 감소시키고 2번으로 돌아가 반복

def gcd(a,b):
    
    i = min(a, b)
    print(i)
    while True:
        if a % i == 0 and b % i == 0:
            return i
        i = i - 1

if __name__ == "__main__":
    print(gcd(4,6))