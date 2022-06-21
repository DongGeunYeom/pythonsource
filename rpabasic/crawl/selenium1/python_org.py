# python.org 접속
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://www.python.org")
browser.maximize_window()

assert "Python" in browser.title
print("소스 가져오기")
print(browser.page_source)

time.sleep(3)
browser.quit()
