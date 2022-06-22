# 네이버 항공권 자동화
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

browser = webdriver.Chrome()
browser.get("https://flight.naver.com/")
browser.maximize_window()
time.sleep(2)

try:
    # 도착 클릭
    browser.find_element(
        By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]'
    ).click()
    time.sleep(1)

    # 국내 클릭
    browser.find_element(
        By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/button[1]'
    ).click()
    time.sleep(1)

    # 제주 클릭
    browser.find_element(
        By.XPATH,
        '//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/div/button[2]',
    ).click()
    time.sleep(1)

    # 가는 날 클릭
    browser.find_element(
        By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]'
    ).click()
    time.sleep(1)

    # 가는 날짜 클릭
    browser.find_element(
        By.XPATH,
        '//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[1]/td[6]/button',
    ).click()

    # 오는 날짜 클릭
    browser.find_element(
        By.XPATH,
        '//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[6]/button',
    ).click()

    # 항공권 검색 클릭
    browser.find_element(
        By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/button'
    ).click()

    # 항공권 검색 결과 출력 (항공사)
    airline = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                "div.domestic_schedule__1Whiq > div > div.heading > div.airline",
            )
        )
    )
    print(airline.text)

except Exception as e:
    print(e)

time.sleep(3)
browser.quit()
