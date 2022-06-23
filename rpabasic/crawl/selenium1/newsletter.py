# 나라장터 용역 공고 자동화
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup

from openpyxl import Workbook

browser = webdriver.Chrome()
browser.get("https://www.naver.com")
browser.maximize_window()

# 새 창 띄우기
browser.execute_script("window.open('http://www.daum.net')")

# 브라우저 리스트로 다루기(네이버, 다음)
tabs = browser.window_handles  # tabs[0] : 네이버 , tabs[1] : 다음
# browser.switch_to.window(tabs[1]) # 다음
# browser.switch_to.window(tabs[0]) # 네이버

time.sleep(5)
browser.quit()
