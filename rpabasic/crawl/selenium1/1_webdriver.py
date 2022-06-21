# pip install selenium
# 셀레니움 - 브라우저 자동화 개념 적용
#           webdriver 이용해서 브라우저 조작, 자동으로 일을 시킬 수 있음
#           웹을 테스트하기 위한 프레임워크
#           자바, 파이썬, C#, 자바스크립트 등 언어들에서 사용 가능

from time import time
from selenium import webdriver


# . : pythonsource 에 크롬 드라이버 위치
browser = webdriver.Chrome()
# 특정 사이트 연결
browser.get("https://www.naver.com")
browser.maximize_window

time.sleep(3)
# 브라우저 닫기
browser.quit()
