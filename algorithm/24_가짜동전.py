# 전체 동전을 a,b / c,d 그룹으로 나눔
# a,b 까지 동전
# c~d 까지 동전

# a~b에 가짜 동전이 있다면 -1 리턴
# c~d에 가짜 동전이 있다면 1 리턴
# 가짜동전이 없다면 0 리턴

# 양팔저울 함수
def weight(a, b, c, d):

    # 임의의 fake 동전 위치
    fake = 29

    # a <= fake and fake <= b
    if a <= fake <= b:
        return -1
    if c <= fake <= d:
        return 1
    return 0


def find_fakecoin(left, right):

    # 종료 조건
    if left == right:
        return left

    half = (right - left + 1) // 2

    # 100개의 동전이 있다고 할 때 0~49가 g1,
    # 50~99가 g2
    g1_left = left
    g1_right = left + half - 1

    g2_left = left + half
    g2_right = g2_left + half - 1

    result = weight(g1_left, g1_right, g2_left, g2_right)

    if result == -1:  # 그룹1에 가짜동전 있음
        return find_fakecoin(g1_left, g1_right)
    elif result == 1:  # 그룹2에 가짜동전 있음
        return find_fakecoin(g2_left, g2_right)
    else:  # 그룹 안에 가짜동전 없음
        return right  # 두 그룹으로 나누지 않고 남은 나머지 한 개의 동전이 가짜


if __name__ == "__main__":
    n = 100
    print(find_fakecoin(0, n - 1))
