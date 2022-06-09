# 키보드 다루기
import pyautogui as p

# 입력 : write()
# p.write("write")

# 메모장에 문자열 타이핑
# 현재 화면에 메모장 활성화
notepad = p.getWindowsWithTitle("제목 없음")[0]
notepad.activate()

# p.write("write")
# p.write("pyautogui", interval=0.5)
# p.write("안녕하세요")  # 한글 지원 안함

# 해야 할 작업을 리스트로 작성
# p.write(
#     ["h", "e", "l", "l", "'o", "left", "left", "left", "right", "l", "o", "enter"],
#     interval=0.25,
# )

# hotkey(조합키)
# import pyperclip  # 클립보드

# pyperclip.copy("안녕하세요")
# p.hotkey("ctrl", "v")
# p.hotkey("ctrl", "a")
# p.hotkey("ctrl", "shift", "esc") # 작업관리자 단축키
# keyDown() + keyUp() == press()
# p.keyDown("shift")
# p.press("4")
# p.keyUp()

p.press(["a", "b", "c"], 2)
p.press(["#", "$"], 2)
