from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# options = webdriver.ChromeOptions()
# options.headless = True
# browser = webdriver.Chrome(options=options) # ElementClickInterceptedException
browser = webdriver.Chrome()
browser.get("https://ecos.bok.or.kr/#/")
time.sleep(4)

# 100대 통계지표 찾기
path = browser.find_element(
    By.XPATH, '//*[@id="root"]/div[5]/div/div[2]/div[4]/div[1]/div[3]/ul/li[1]/a'
)
path.click()
time.sleep(3)

# 엑셀 다운로드 버튼 찾기
browser.find_element(By.CSS_SELECTOR, "div.exelDown.partition-right > button").click()

time.sleep(3)
browser.quit()
