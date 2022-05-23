# 주차장 프로그램
# 1. 메뉴 제공 : [1] 자동차 넣기 | [2] 자동차 빼기 | [3] 종료 :
# 2. 사용자는 1~3 메뉴만 선택가능
# 3. 1번을 선택한 경우 다음과 같은 출력 : A~E 까지 자동차 들어감. 주차장 상태 ==> [] 리스트화 / 주차장 꽉 참
# 4. 2번을 선택한 경우 : A~E 까지 자동차 나감. 주차장 상태 ==> [] 리스트화 / 빠져나갈 자동차가 없음
# 5. 3번을 선택한 경우 : 프로그램 종료

parking_lot = []
top, car_name = 0, "A"
# ord("A") => 65
# chr(64) => A
print(ord(car_name))
print(ord(car_name)+1)
print(chr(ord(car_name)+2))
while True:
    no = int(input("[1] 자동차 넣기 | [2] 자동차 빼기 | [3] 종료 " ))

    if no <= 3:
        if no == 1:
            if top >= 5 :
                print("주차장 꽉 찼음")
            else:
                parking_lot.append(car_name)
                print("{} 자동차 들어감. 주차장 상태 ==> {}".format(car_name, parking_lot))

                top += 1
                car_name = chr(ord(car_name)+1)
        elif no == 2:
            if top == 0:
                print("빠져나갈 자동차가 없음")
            else:
                out_car = parking_lot.pop()
                print("{} 자동차 나감. 주차장 상태 ==> {}".format(out_car, parking_lot))

                top -= 1
                car_name = chr(ord(car_name)-1)
        elif no == 3:
            print("프로그램 종료")
            break
    else:
        print("번호를 확인해 주세요")