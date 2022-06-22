# 구글 이미지 다운로드
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from urllib.request import urlretrieve  # 다운로드 전용

browser = webdriver.Chrome()
browser.get("https://www.google.com/imghp?hl=ko")
browser.maximize_window()
time.sleep(1)

# 이미지 입력 가져오기
element = browser.find_element(By.NAME, "q")
element.send_keys("python")
element.send_keys(Keys.ENTER)

# 2초에 한 번씩 스크롤 이동
interval = 2

# 현재 문서 높이 가져와서 저장
prev_height = browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

while True:
    # 스크롤 이동
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # 페이지 로딩 대기
    time.sleep(interval)

    # 스크롤이 진행된 후 현재 문서 높이
    curr_height = browser.execute_script("return document.body.scrollHeight")

    if curr_height == prev_height:
        try:
            # 결과 더 보기 버튼
            browser.find_element(By.CLASS_NAME, "mye4qd").click()
        except:
            break

    prev_height = curr_height

# 화면에 나온 작은 이미지들 요소 찾기
images = browser.find_elements(By.CSS_SELECTOR, "div.bRMDJf.islir > img")
count = 1

for image in images:
    try:
        # 이미지 저장
        image.click()
        time.sleep(2)

        # 큰 이미지 요소 찾기
        imgUrl = browser.find_element(
            By.XPATH,
            '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img',
        ).get_attribute("src")

        urlretrieve(imgUrl, "./rpabasic/crawl/image/" + str(count) + ".jpg")
        count += 1

    except Exception as e:
        print("이미지 저장 실패")

time.sleep(3)
browser.quit()
