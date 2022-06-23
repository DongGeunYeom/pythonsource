from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


browser = webdriver.Chrome()
browser.get("http://prod.danawa.com/list/?cate=112758&15main_11_02")
browser.maximize_window()
time.sleep(2)

# 제조사 더보기 클릭
WebDriverWait(browser, 3).until(
    EC.presence_of_element_located(
        (By.XPATH, '//*[@id="dlMaker_simple"]/dd/div[2]/button[1]')
    )
).click()

# 애플
WebDriverWait(browser, 3).until(
    EC.presence_of_element_located(
        (By.XPATH, '//*[@id="selectMaker_simple_priceCompare_A"]/li[17]/label')
    )
).click()

# 제품 목록이 화면에 로딩되도록 대기
time.sleep(2)

# print(browser.page_source)

# 상품 정보 추출 - 상품명, 가격(첫 번째), 이미지 src
# productNames = browser.find_elements(By.NAME, "productName")
product_list = browser.find_elements(
    By.CSS_SELECTOR,
    "div.main_prodlist_list > ul > li:not(.prod_ad_item):not(.product-pot)",
)

idx = 1
for product in product_list:
    # 제품명
    product_name = product.find_element(By.CSS_SELECTOR, "p > a").text.strip()

    # 가격
    product_price = product.find_element(
        By.CSS_SELECTOR, "p.price_sect > a"
    ).text.strip()

    # 이미지 경로
    product_image = product.find_element(By.CSS_SELECTOR, ".thumb_image img")

    if product_image.get_attribute("data-original"):
        product_image = product_image.get_attribute("data-original")
    else:
        product_image = product_image.get_attribute("src")

    print(idx, product_name, product_price, product_image)
    idx += 1
    time.sleep(1)


time.sleep(3)
browser.quit()
