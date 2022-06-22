# python.org 접속
from turtle import title
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.maximize_window()

browser.get("http://www.python.org")

# 검색 창 찾기
element = browser.find_element(By.ID, "id-search-field")

# 검색 창 초기화
element.clear()  # 검색어 입력
element.send_keys("python")

# 엔터 입력
element.send_keys(Keys.ENTER)
time.sleep(1)

# 결과 페이지에서 원하는 요소 추출
# titles = browser.find_elements(By.TAG_NAME, "h3")

# for title in titles:
#     print(title.text)

# BeautifulSoup 이용하는 방식
res = BeautifulSoup(browser.page_source, "lxml")
titles = res.find_all("h3")

for title in titles:
    print(title.get_text())

time.sleep(3)
browser.quit()
