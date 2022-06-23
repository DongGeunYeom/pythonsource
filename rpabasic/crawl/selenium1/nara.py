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

# 업무, 공고번호, 분류, 공고명, 공고기관, 수요기관, 계약방법, 입력일시, 마감일시, 원문상세주소
wb = Workbook()
ws = wb.active
ws.title = "나라용역공고"
ws.append(["업무", "공고번호", "분류", "공고명", "공고기관", "수요기관", "계약방법", "입력일시", "마감일시", "원문상세주소"])
ws.column_dimensions["B"].width = 16  # 공고번호
ws.column_dimensions["D"].width = 75  # 공고명
ws.column_dimensions["E"].width = 45  # 공고기관
ws.column_dimensions["F"].width = 45  # 수요기관
ws.column_dimensions["G"].width = 39  # 계약방법
ws.column_dimensions["H"].width = 16  # 입력일시
ws.column_dimensions["I"].width = 17  # 마감일시
ws.column_dimensions["J"].width = 108  # 원문상세주소

# https://www.g2b.go.kr:8101/ep/tbid/tbidList.do?taskClCds=&bidNm=&searchDtType=1&fromBidDt=2022/05/24&toBidDt=2022/06/23&fromOpenBidDt=&toOpenBidDt=&radOrgan=1&instNm=&area=&regYn=Y&bidSearchType=1&searchType=1
# taskClCds = 5 용역
# fromBidDt, toBidDt, currentPageNo

browser = webdriver.Chrome()
browser.maximize_window()
for i in range(1, 4):
    url = "https://www.g2b.go.kr:8101/ep/tbid/tbidList.do?searchType=1&bidSearchType=1&taskClCds=5&bidNm=&"
    url += "searchDtType=1&fromBidDt=2022%2F05%2F24&toBidDt=2022%2F06%2F23&fromOpenBidDt=&toOpenBidDt=&"
    url += "radOrgan=1&instNm=&instSearchRangeType=&refNo=&area=&areaNm=&strArea=&orgArea=&industry=&"
    url += "industryCd=&upBudget=&downBudget=&budgetCompare=&detailPrdnmNo=&detailPrdnm=&procmntReqNo=&"
    url += (
        "intbidYn=&regYn=Y&recordCountPerPage=30&currentPageNo="
        + str(i)
        + "&maxPageViewNoByWshan=2&"
    )

    browser.get(url)
    time.sleep(2)

    # 업무, 공고번호, 분류, 공고명, 공고기관, 수요기관, 계약방법, 입력일시(입찰마감일시)
    tbody = browser.find_element(By.XPATH, '//*[@id="resultForm"]/div[2]/table/tbody')
    trs = tbody.find_elements(By.TAG_NAME, "tr")
    for idx, row in enumerate(trs):
        # 업무
        data_1 = row.find_elements(By.TAG_NAME, "td")[0]
        # 공고번호
        data_2 = row.find_elements(By.TAG_NAME, "td")[1]
        # 분류
        data_3 = row.find_elements(By.TAG_NAME, "td")[2]
        # 공고명
        data_4 = row.find_elements(By.TAG_NAME, "td")[3]
        # 공고기관
        data_5 = row.find_elements(By.TAG_NAME, "td")[4]
        # 수요기관
        data_6 = row.find_elements(By.TAG_NAME, "td")[5]
        # 계약방법
        data_7 = row.find_elements(By.TAG_NAME, "td")[6]
        # 입력일시(+마감일시)
        # 2022/06/05 17:44 <br>
        # (2022/06/15 10:00)
        data_8 = row.find_elements(By.TAG_NAME, "td")[7]

        # 입력일시와 마감일시 따로 작업
        reg_date = data_8.text.split("\n")[0]
        end_date = data_8.text.split("\n")[1]

        # 입찰공고 상세보기 (a 태그 가져오기)
        data_link = row.find_element(By.TAG_NAME, "a").get_attribute("href")

        ws.append(
            [
                data_1.text,
                data_2.text,
                data_3.text,
                data_4.text,
                data_5.text,
                data_6.text,
                data_7.text,
                reg_date,
                end_date,
                data_link,
            ]
        )
        time.sleep(1)

wb.save("./rpabasic/crawl/download/nara.xlsx")
wb.close()
time.sleep(3)
browser.quit()
