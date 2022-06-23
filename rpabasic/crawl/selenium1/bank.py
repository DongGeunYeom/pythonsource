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
from openpyxl.drawing.image import Image

browser = webdriver.Chrome()
browser.get("https://www.kebhana.com/cont/mall/mall15/mall1503/index.jsp")
browser.maximize_window()
time.sleep(1)

# iframe 안으로 들어가기
browser.switch_to.frame("bankIframe")

# 기간환율변동 클릭
browser.find_element(
    By.XPATH, '//*[@id="inqFrm"]/table/tbody/tr[1]/td/span/p/label[3]'
).click()  # NoSuchElementException (iframe)

# 시작일자 (20220523)
# browser.find_element(By.XPATH, '//*[@id="chkDiv_p"]/td/div[2]/div[1]/a').click()
# browser.find_element(
#     By.XPATH, '//*[@id="OPB_calendar_month_prev_generatedByJS"]'
# ).click()
# browser.find_element(
#     By.XPATH, '//*[@id="OPB_calendar_table_generatedByJS"]/tr[4]/td[2]/a'
# ).click()
start_date = browser.find_element(By.ID, "tmpInqStrDt_p")
start_date.clear()
start_date.send_keys("20220523")

# 종료일자 (20220622)
end_date = browser.find_element(By.ID, "tmpInqEndDt_p")
end_date.clear()
end_date.send_keys("20220622")

# 통화선택 => 유로 클릭
browser.find_element(By.ID, "curCd").send_keys("EUR:유로(유럽연합)")

# 고시회차 => 최종 클릭
browser.find_element(
    By.XPATH, '//*[@id="inqFrm"]/table/tbody/tr[6]/td/span/p/label[2]'
).click()

# 조회버튼 클릭
browser.find_element(By.XPATH, '//*[@id="HANA_CONTENTS_DIV"]/div[2]/a/span').click()

time.sleep(0.5)

# 엑셀 다운로드 버튼 클릭
browser.find_element(By.XPATH, '//*[@id="searchContentDiv"]/div[1]/a[2]').click()


time.sleep(3)
browser.quit()
