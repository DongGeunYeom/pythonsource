from cmath import e
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.maximize_window()

browser.get("http://www.naver.com")
time.sleep(1)

# 두 번째 탭을 연 후에 daum 접속
# 스크립트 새창 열기
browser.execute_script("window.open('http://www.daum.net')")

print("1. title {}".format(browser.title))  # NAVER

# 현재 브라우저에 열린 탭 가져오기
tabs = browser.window_handles  # tabs[0] : 처음 접속 페이지

browser.switch_to.window(tabs[1])
print("2. title {}".format(browser.title))

element = browser.find_element(By.NAME, "q")
element.send_keys("아이폰")
element.send_keys(Keys.ENTER)

time.sleep(1)

# 네이버로 돌아오기
browser.switch_to.window(tabs[0])

time.sleep(3)
browser.quit()
