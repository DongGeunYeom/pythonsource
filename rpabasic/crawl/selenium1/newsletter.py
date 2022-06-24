# 뉴스레터 보내기 자동화
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup

import requests
import pyperclip
from openpyxl import Workbook

browser = webdriver.Chrome()
browser.get("https://www.naver.com")
browser.maximize_window()

# 새 창 띄우기
browser.execute_script("window.open('http://www.daum.net')")

# 브라우저 리스트로 다루기(네이버, 다음)
tabs = browser.window_handles  # tabs[0] : 네이버 , tabs[1] : 다음
# browser.switch_to.window(tabs[1]) # 다음

# 첫 번째 탭 선택
browser.switch_to.window(tabs[0])  # 네이버

# 검색어 넣기
keyword = "RPA 파이썬"
browser.find_element(By.NAME, "query").send_keys(keyword)

# 검색버튼 클릭
browser.find_element(By.ID, "search_btn").click()

# 결과 기다리기
time.sleep(1)

# 뉴스 메뉴 클릭
browser.find_element(By.XPATH, '//*[@id="lnb"]/div[1]/div/ul/li[8]/a').click()
time.sleep(0.5)

# 최신순 클릭
browser.find_element(By.XPATH, '//*[@id="snb"]/div[1]/div/div[1]/a[2]').click()

# 조회일 기준으로 뉴스 건수 가져오기
client_id = "Hj3r1GGUiiu9JIwInsa3"
client_secret = "ZIX8dh0JJT"

url = "https://openapi.naver.com/v1/search/news.json"

headers = {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret}
param = {"query": keyword}
res = requests.get(url, headers=headers, params=param)
result = res.json()

# 뉴스 총 건수 변수 지정하고 파일로 저장하기
news_total_cnt = result.get("total")  # result['total']

# 1) 기존 뉴스 건수를 읽어와서 비교하기
path = "./rpabasic/crawl/selenium1/totalCnt.txt"
with open(path, "r") as f:
    old_total_cnt = int(f.readline())

# 2) new_total_cnt 와 기존 뉴스건수 비교 => 지난 뉴스건수와 차이 구하기(new_add_cnt)
# 147 - 0
if news_total_cnt > old_total_cnt:
    new_add_cnt = news_total_cnt - old_total_cnt

    # 3) new_total_cnt를 totalCnt.txt에 기록
    with open(path, "w") as f:
        f.write(str(new_add_cnt))
else:
    new_add_cnt = 0

# 페이지 수 지정
if new_add_cnt == 0:
    page_cnt = 0
else:
    page_cnt = new_add_cnt // 10 + 1

start, num = 1, 1
result = ""

if page_cnt == 0:
    for i in range(3):

        start = start + (i * 10)

        url = "https://search.naver.com/search.naver?where=news&"
        url += "query=" + keyword + "&sm=tab_opt&sort=1&photo=0&field=0&pd=0&ds=&"
        url += "de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&"
        url += "nso=so%3Add%2Cp%3Aall&is_sug_officeid=0&start=" + str(start)

        browser.get(url)

        # 뉴스 크롤링
        # 뉴스제목, 매체, 등록일, 원문 주소
        news_area = browser.find_elements(By.CLASS_NAME, "news_area")

        for idx, news in enumerate(news_area):
            # 뉴스 제목
            title = news.find_element(By.CLASS_NAME, "news_tit")
            # 매체
            press = news.find_element(By.CLASS_NAME, "press")
            # 등록일
            reg_date = news.find_element(By.CSS_SELECTOR, ".info_group > span")
            # 원문주소
            news_url = title.get_attribute("href")

            # print(
            #     "{}, {}, {}, {}, {}".format(
            #         idx, title.text, press.text, reg_date.text, news_url
            #     )
            # )
            result += "<div><p><a href='" + news_url + "'>" + title.text + "</a> "
            result += press.text + " " + reg_date.text + "</p></div>"


# 다음에서 이메일 보내기
# 두 번째 탭으로 이동
browser.switch_to.window(tabs[1])

# 다음 로그인
# 카카오계정으로 로그인 클릭
browser.find_element(By.CLASS_NAME, "link_kakaoid").click()
time.sleep(0.5)

userid = "meronot@naver.com"
password = "rptksqud1a"
# 아이디 입력
id_block = browser.find_element(By.ID, "id_email_2")
id_block.clear()
id_block.send_keys(userid)

# 비밀번호 입력
pwd_block = browser.find_element(By.ID, "id_password_3")
pwd_block.clear()
pwd_block.send_keys(password)

# 로봇이 아닙니다 클릭
# 이거 난 안뜨던데... 테스트 할 땐 안뜸.. 뭐임 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
reCAPTCHA = browser.find_element(By.CLASS_NAME, "txt_check.tooltip_link")
try:
    # 로그인 클릭
    browser.find_element(
        By.CSS_SELECTOR,
        "#login-form > fieldset > div.wrap_btn > button.btn_g.btn_confirm.submit",
    ).click()
except:
    reCAPTCHA.click()
    browser.find_element(
        By.CSS_SELECTOR,
        "#login-form > fieldset > div.wrap_btn > button.btn_g.btn_confirm.submit",
    ).click()


time.sleep(1)

# 메일 클릭
browser.find_element(By.CLASS_NAME, "link_num").click()
time.sleep(1)

# result 내용 copy
pyperclip.copy(result)

# 메일쓰기 클릭
browser.find_element(By.CLASS_NAME, "btn_comm.btn_write").click()
time.sleep(0.5)

getter = "meronot@naver.com"
getter_title = "귀하는 행운의 편지를 받으셨습니다."

# 받는사람 입력
mail_to = browser.find_element(By.ID, "toTextarea")
mail_to.clear()
mail_to.send_keys(getter)

# 제목 입력
mail_title = browser.find_element(By.ID, "mailSubject")
mail_title.click()
mail_title.clear()
mail_title.send_keys(getter_title)

# 하단의 HTML 탭 클릭 + iframe 이동
browser.switch_to.frame("tx_canvas_wysiwyg")
bottom_html = browser.find_element(By.CLASS_NAME, "tx-content-container")
bottom_html.click()
bottom_html.send_keys(Keys.CONTROL, "v")
time.sleep(1)

# 보내기 클릭 + iframe 돌아오기
browser.switch_to.default_content()
browser.find_element(By.CLASS_NAME, "btn_toolbar.btn_write").click()

time.sleep(5)
browser.quit()
