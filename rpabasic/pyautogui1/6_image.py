# 이미지 인식
import pyautogui as p

# confidence : 신뢰도(default 1, 0.8 ~ 0.9로 설정) - opencv-python 라이브러리 설치 -> 신뢰도 설정
# locateOnScreen() : 캡쳐한 이미지의 화면상 좌표 구하기
# 이미지 기반이어서 해상도가 바뀌는 경우 등에는 잘 안됨
# 이미지 파일명은 영문으로 작성

# screen_locate = p.locateOnScreen("./rpabasic/pyautogui1/file_menu.png", confidence=0.9)
# print(screen_locate)  # Box(left=1370, top=1, width=56, height=31)

# locateAllOnScreen() : 찾아야 하는 이미지가 여러 개 있는경우
# p.sleep(2)
# for i in p.locateAllOnScreen("./rpabasic/pyautogui1/checkbox.png", confidence=0.9):
#     print(i)
#     p.click(i)

# 찾아야 하는 대상이 화면에 늦게 나타나는 경우

# 찾을 때까지 반복시키기
# file_menu = p.locateOnScreen("./rpabasic/pyautogui1/checkbox.png", confidence=0.9)

# while file_menu is None:
#     file_menu = p.locateOnScreen("./rpabasic/pyautogui1/checkbox.png", confidence=0.9)
#     print("발견할 수 없음")

# p.click(file_menu)

# 일정한 시간만큼만 기다리기
import time, sys

timeout = 15
start = time.time()

file_menu = p.locateOnScreen("./rpabasic/pyautogui1/checkbox.png", confidence=0.9)
while file_menu is None:
    file_menu = p.locateOnScreen("./rpabasic/pyautogui1/checkbox.png", confidence=0.9)

    end = time.time()

    if end - start > timeout:
        print("시간 종료")
        sys.exit()

p.click(file_menu)
