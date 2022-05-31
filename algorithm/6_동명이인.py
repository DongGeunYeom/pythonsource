# 동명이인 찾기
# ["Tom","Jerry", "Mike", "Tom"]

# n명의 사람 이름 중에서 같은 이름을 찾아 집합으로 만들어 돌려주는 알고리즘 작성
# 알고리즘 입력 : n명의 이름이 들어있는 리스트 ["Tom", "Jerry", "Mike", "Tom"]
#         결과 : 같은 이름들이 들어 있는 집합 {"Tom"}

# Tom 입장 : 3번 비교
# Jerry 입장 : 2번 비교
# Mike 입장 : 1번 비교
# 마지막 Tom : 0번 비교

# 계산 복잡도 O(n제곱)

# def dup_name(list1):
#     result = set()

#     for n in list1:
#         if list1.count(n) > 1:
#             result.add(n)
#     # 튜플이기 때문에 중복 값은 제거가 됩니다... 맞을까요
#     return result

def dup_name(list1):
    result = set()
    size = len(list1)

    for i in range(0, size-1):
        for j in range(i+1, size):
            if list1[i] == list1[j]:
                result.add(list1[i])

    return result


if __name__ == "__main__":
    list1 = ["Tom","Jerry", "Mike", "Tom", "Michael", "Jerri"]
   
    print(dup_name(list1))