from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://www.daum.net")
browser.maximize_window()

print(browser.current_url)  # https://www.daum.net/
print(browser.title)  # Daum

# 테스트 코드에서 오류가 발생하면 이후 코드는 실행 안함
assert "Daum" in browser.title

# print(browser.page_source)
time.sleep(3)
browser.quit()
