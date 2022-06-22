# 검색어 넣고 검색결과 출력
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()

# 브라우저 창을 띄우지 않음
options.headless = True

browser = webdriver.Chrome(options=options)
browser.get("https://www.youtube.com/")

time.sleep(2)

# 검색 입력 공간 찾기
search = browser.find_element(By.NAME, "search_query")
search.send_keys("아이유")
search.send_keys(Keys.ENTER)
time.sleep(2)

# 검색 결과 출력
titles = browser.find_elements(By.TAG_NAME, "h3")
for title in titles:
    print(title.text)

# res = BeautifulSoup(browser.page_source, "lxml")
# titles = res.find_all("h3")

# for title in titles:
#     print(title.get_text())

time.sleep(3)
browser.quit()
