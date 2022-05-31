# 리스트 안에서 가장 큰 숫자 찾기
# [17,92,18,33,58,7,33,42]

def find_max(list1):
    # 리스트 첫번쨰 요소 max에 담기
    max = list1[0]
    # 리스트 사이즈 확인
    size = len(list1)
    
    for i in range(1, size):
        if max < list1[i]:
            max = list1[i]
    return max

def find_max2(list1):
    max = 0

    for n in list1:
        if n > max:
            max = n
    return max
       

# 가장 큰 값이 있는 위치번호 돌려받기
def find_max1(list1):
    # 리스트 0번 index 를 max_idx에 담기
    max_idx = 0
    # 리스트 사이즈 확인
    size = len(list1)
    
    for i in range(1, size):
        if list1[max_idx] < list1[i]:
            max_idx = i
            
    return max_idx
    
    
if __name__ == "__main__":
    list1 = [17,92,18,33,58,7,33,42]

    print("가장 큰 숫자 ", find_max(list1))
    max_idx = find_max1(list1)
    print("가장 큰 숫자가 있는 위치 {}, 가장 큰 숫자 {} ".format(max_idx, list1[max_idx]))
    print("가장 큰 숫자 ", find_max2(list1))
