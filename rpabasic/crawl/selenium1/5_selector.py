from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.maximize_window()

browser.get("http://www.python.org")

# 결과 페이지에서 원하는 요소 찾기 - 기준 부여
# find_element() : 하나의 요소찾기
# find_elements() : 여러 개의 요소 찾기

# 기준 - By
# By.NAME, By.CLASS_NAME, By.CSS_SELECTOR, By.ID, By.LINK_TEXT, By.PARTIAL_LINK_TEXT,
# By.TAG_NAME, By.XPATH

# 아이디 값으로 찾기
# element = browser.find_element(By.ID, "id-search-field")

# css 선택자로 찾기
# element = browser.find_element(By.CSS_SELECTOR, "#id-search-field")

# 클래스이름으로 찾기
# element = browser.find_element(By.CLASS_NAME, "search-field")


# xpath로 찾기
element = browser.find_element(By.XPATH, '//*[@id="id-search-field"]')

element.send_keys("python")
element.send_keys(Keys.ENTER)

time.sleep(3)
browser.quit()
