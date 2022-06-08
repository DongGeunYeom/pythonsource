# 이미지 인식
import pyautogui as p

# locateOnScreen() : 캡쳐한 이미지의 화면상 좌표 구하기
# 이미지 기반이어서 해상도가 바뀌는 경우 등에는 잘 안됨
# 이미지 파일명은 영문으로 작성

screen_locate = p.locateOnScreen("./rpabasic/pyautogui1/file_menu.png")
print(screen_locate)  # Box(left=1370, top=1, width=56, height=31)
