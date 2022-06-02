# 병합정렬 : 분해, 병합


def merge_sort1(list1):
    # 리스트 크기 구하기
    size = len(list1)

    # 종료 조건
    if size <= 1:
        return list1

    # 분해작업
    mid = size // 2  # 중간구하기

    g1 = merge_sort1(list1[:mid])  # 재귀호출로 첫번째 그룹 [6,8,3,9,10] => g1 [6,8], g2 [3,9,10]
    g2 = merge_sort1(list1[mid:])  # [1,2,4,7,5]

    # 병합 작업
    # python 리스트가 비어 있으면 False
    result = []
    while g1 and g2:
        if g1[0] < g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))

    # 자료 비교 후 남아있는 요소를 추가
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))

    return result


if __name__ == "__main__":
    list1 = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
    print(merge_sort1(list1))
