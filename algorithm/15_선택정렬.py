# 선택정렬 : 정렬 알고리즘 중 쉬운 방법

# 이중 for 문 사용


def selection_sort3(list1):
    for i in range(len(list1) - 1):
        for j in range(i + 1, len(list1)):
            if list1[i] > list1[j]:
                list1[i], list1[j] = list1[j], list1[i]
    return list1


# 오름차순
def selection_sort1(list1):
    size = len(list1)

    for i in range(0, size - 1):  # 0, 1, 2, 3
        min_idx = i
        for j in range(i + 1, size):  # 최소값의 위치 찾기
            if list1[j] < list1[min_idx]:
                min_idx = j

        # 찾은 최소값과 정렬위치를 교환
        list1[i], list1[min_idx] = list1[min_idx], list1[i]

    return list1


# 내림차순
def selection_sort2(list1):
    size = len(list1)

    for i in range(0, size - 1):  # 0, 1, 2, 3
        max_idx = i
        for j in range(i + 1, size):  # 최소값의 위치 찾기
            if list1[j] > list1[max_idx]:
                max_idx = j

        # 찾은 최소값과 정렬위치를 교환
        list1[i], list1[max_idx] = list1[max_idx], list1[i]

    return list1


if __name__ == "__main__":
    list1 = [35, 9, 2, 85, 17]

    print("오름차순 ", selection_sort1(list1))
    print("내림차순 ", selection_sort2(list1))

    print("오름차순 ", selection_sort3(list1))
