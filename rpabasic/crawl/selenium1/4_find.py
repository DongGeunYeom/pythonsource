# python.org 접속
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("http://www.daum.net")
browser.maximize_window()

assert "Daum" in browser.title
print("소스 가져오기")
element = browser.find_element(By.NAME, "q")
# print(element) # <selenium.webdriver.remote.webelement.WebElement (session="0f1a2c073b0b9a8939ba25755d01e04d", element="763dc702-6d8e-4282-9559-cd6102757cc1")>
element.send_keys("아이폰")
element.send_keys(Keys.ENTER)

time.sleep(3)
browser.quit()
