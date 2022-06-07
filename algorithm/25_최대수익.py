# 최대수익
# 입력 : 주식 가격 변화 리스트
# 출력 : 한 주를 사고 팔아 얻을 수 있는 최대 수익


def get_max(stock):
    size = len(stock)
    max_profit = 0

    for i in range(size - 1):
        for j in range(i + 1, size):
            profit = stock[j] - stock[i]
            if profit > max_profit:
                max_profit = profit
    return max_profit


def get_max2(stock):
    size = len(stock)
    max_profit = 0
    # 첫째 날의 주가를 최솟값으로 시작
    min_price = stock[0]

    for i in range(1, size):
        profit = stock[i] - min_price
        if profit > max_profit:
            max_profit = profit
        if stock[i] < min_price:
            min_price = stock[i]

    return max_profit


if __name__ == "__main__":
    stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
    print("최대수익", get_max2(stock))
