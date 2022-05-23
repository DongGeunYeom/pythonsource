# tuple
# 리스트와 비슷
# ()로 둘러싸여 있다
# 리스트는 값의 생성, 삭제, 수정이 가능하지만 튜플은 변경이 불가함

# 생성
t1 = ()
t2 = (1,2,3)
t3 = (1,) # 1개의 요소만을 가질 때 요소 뒤에 콤마 반드시 필요
t4 = 4,5,6 # 여러 개 요소가 존재시 괄호 생략 가능
t5 = ("a","b","c",("d","e"))

print(t1)
print(t2)
print(t3)
print(t4)
print(t5)

# del t2[1] # TypeError: 'tuple' object doesn't support item deletion

# t2[1] = 5 # TypeError: 'tuple' object does not support item assignment