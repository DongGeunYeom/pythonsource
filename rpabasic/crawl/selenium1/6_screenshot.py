from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.maximize_window()

browser.get("http://www.daum.net")

# 관련 검색어 추출
search = browser.find_element(By.NAME, "q")
search.send_keys("방탄소년단")
search.send_keys(Keys.ENTER)
time.sleep(2)

lists_top = browser.find_elements(By.CSS_SELECTOR, "#netizen_lists_top > span.wsn")

for item in lists_top:
    print(item.text)

# 현재 화면 캡쳐
browser.save_screenshot("./rpabasic/crawl/download/image.png")


time.sleep(3)
browser.quit()
