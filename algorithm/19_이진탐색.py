# 이진탐색
# 자료가 정렬된 상태여야 함

def binary_search1(list1, number):
    # 시작위치 지정
    start = 0

    # 종료위치 지정
    end = len(list1) -1

    # 반복문 - 시작위치가 종료위치보다 작거나 같을 때까지
    while start <= end:
        # 중간위치 지정
        idx = (start + end) // 2

         # 찾고자 하는 숫자가 중간위치의 숫자보다 작으면 end = 중간위치 - 1
        if number < list1[idx]:
            print(list1[idx])
            end = idx - 1 
        # 찾고자 하는 숫자가 중간위치의 숫자보다 크면 start = 중간위치 + 1
        elif number > list1[idx]:
            print(list1[idx])
            start = idx + 1
        # 둘 다 아닌 경우 중간위치 리턴
        else:
            return idx

# 재귀호출
# 종료조건 : 리스트가 빈 상태라면 탐색종료
# 재귀 : 1) 중간 위치 지정
#        2) 찾는 값과 중간위치 값이 같다면 결과값으로 중간 위치 값 돌려주기
#        3) 찾는 값이 중간 위치 값보다 크다면 중간 위치의 오른쪽을 대상으로 이진탐색 함수를 재귀호출하기
#        4) 찾는 값이 중간 위치 값보다 작다면 중간 위치의 왼쪽을 대상으로 이진탐색 함수를 재귀호출하기
def binary_search2(list1, number, start, end):
    # 중간위치 지정
    idx = (start+end) // 2

    # 반복문 - 시작위치가 종료위치보다 작거나 같을 때까지
    if list1 == [] or number not in list1:
        return

    # 찾고자 하는 숫자가 중간위치의 숫자보다 작으면 중간 위치의 왼쪽을 대상으로 이진탐색 함수를 재귀호출하기
    if number < list1[idx]:
        return binary_search2(list1, number, start, idx-1)

    # 찾고자 하는 숫자가 중간위치의 숫자보다 크면 중간 위치의 오른쪽을 대상으로 이진탐색 함수를 재귀호출하기
    elif number > list1[idx]:
         return binary_search2(list1, number, idx+1, end)

        # 둘 다 아닌 경우 중간위치 리턴
    else:
        return idx

if __name__ == "__main__":
    list1 = [1,4,9,16,25,36,49,64,81]
    print("36이 있는 위치 ",binary_search1(list1,36))
    print("49가 있는 위치 ",binary_search2(list1, 49, 0, len(list1)-1))