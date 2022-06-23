from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.get("http://prod.danawa.com/list/?cate=112758&15main_11_02")
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

# 상품 정보 추출 - 상품명, 가격(첫 번째), 이미지 src
# product_list = browser.find_elements(
#     By.CSS_SELECTOR, "div.main_prodlist_list > ul > li:not(.prod_ad_item):not(.product-pot)"
# )

# 현재 페이지 / 크롤링할 페이지 수 지정
curr_page, target_crawl_num = 1, 6

idx = 1
while curr_page <= target_crawl_num:

    # print(browser.page_source)
    soup = BeautifulSoup(browser.page_source, "lxml")

    product_list = soup.select(
        "div.main_prodlist_list > ul > li:not(.prod_ad_item):not(.product-pot)"
    )

    # 현재 페이지 출력
    print("============================ Current Page : {}".format(curr_page))

    # 상품 정보 데이터 얻어와서 출력하는 부분
    for product in product_list:
        # 제품명
        # product_name = product.find_element(By.CSS_SELECTOR, "p > a").text.strip()
        product_name = product.select_one("p > a").text.strip()

        # 가격
        # product_price = product.find_element(By.CSS_SELECTOR, "p.price_sect > a").text.strip()
        product_price = product.select_one("p.price_sect > a").text.strip()

        # 이미지 경로
        # product_image = product.find_element(By.CSS_SELECTOR, ".thumb_link img")

        # if product_image.get_attribute("data-original"):
        #     product_image = product_image.get_attribute("data-original")
        # else:
        #     product_image = product_image.get_attribute("src")

        product_image = product.select_one(".thumb_image img")

        if product_image.get("data-original"):
            product_image = product_image.get("data-original")
        else:
            product_image = product_image.get("src")

        if "http:" not in product_image:
            product_image = "http:" + product_image

        print(idx, product_name, product_price, product_image)
        idx += 1

    print()
    browser.save_screenshot(
        "./rpabasic/crawl/download/target_page{}.png".format(curr_page)
    )

    # 현재 페이지 번호 변경
    curr_page += 1

    if curr_page > target_crawl_num:
        print("크롤링 성공")
        break

    # 다음 페이지 클릭
    # #productListArea > div.prod_num_nav > div > div > a:nth-child(2)
    # #productListArea > div.prod_num_nav > div > div > a:nth-child(3)
    WebDriverWait(browser, 2).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div.number_wrap > a:nth-child({})".format(curr_page))
        )
    ).click()

    # soup 삭제
    del soup

    # 다음 페이지 로딩될 때까지 기다리기
    time.sleep(3)

time.sleep(3)
browser.quit()
