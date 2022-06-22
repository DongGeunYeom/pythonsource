from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("http://www.danawa.com/")

browser.maximize_window()
time.sleep(1)

# 로그인 버튼 찾기
element = browser.find_element(By.CLASS_NAME, "btn_user--login")
element.click()
time.sleep(1)

# 아이디 입력 찾기
userid = browser.find_element(By.ID, "danawa-member-login-input-id")
userid.clear()
userid.send_keys("meronot1")

# 비밀번호 입력 찾기
password = browser.find_element(By.ID, "danawa-member-login-input-pwd")
password.clear()
password.send_keys("rptksqud1%")
password.send_keys(Keys.ENTER)

time.sleep(3)
browser.quit()
