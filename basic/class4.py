class Car:
    """
    UserInfo class
    Author : 홍길동
    Date : 2022-05-26
    Description : 클래스 작성법
    """

    # 클래스 변수
    car_count = 0

    def __init__(self, count, color, speed) -> None:
        self.color = color
        self.speed = speed

        Car.car_count += count

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value

    def chgColor(self, value):
        self.color = value

    def __del__(self):
        Car.car_count -= 1


# 객체 생성

car1 = Car(1, "Red", 20)
car1.upSpeed(50)
print(
    "자동차1 현재 속도 {}km 색상 : {}, 생산된 자동차 대수 : {}대".format(
        car1.speed, car1.color, Car.car_count
    )
)

car2 = Car(1, "Black", 30)
car2.upSpeed(80)
print(
    "자동차2 현재 속도 {}km 색상 : {}, 생산된 자동차 대수 : {}대".format(
        car2.speed, car2.color, Car.car_count
    )
)

car3 = Car(1, "Yellow", 0)
car3.upSpeed(180)
print(
    "자동차2 현재 속도 {}km 색상 : {}, 생산된 자동차 대수 : {}대".format(
        car3.speed, car3.color, Car.car_count
    )
)

del car1
print(Car.car_count)
