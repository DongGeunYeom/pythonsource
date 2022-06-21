from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# pip install webdriver-manager
# 현재 브라우저 버전에 맞는 웹드라이버를 다운로드 받지 않아도 됨


def set_chrome_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return driver


if __name__ == "__main__":
    driver = set_chrome_driver()
    driver.get("https://www.naver.com")
