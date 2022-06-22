from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.maximize_window()

browser.get(
    "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio"
)
time.sleep(1)

# iframe 안의 태그 찾기
# iframe 안으로 들어가서 찾아야 함
browser.switch_to.frame("iframeResult")
element = browser.find_element(By.ID, "html")
element.click()
time.sleep(1)

# iframe 밖으로 나오기
browser.switch_to.default_content()
# 왼쪽에 있던 요소 찾기
left = browser.find_element(
    By.XPATH,
    '//*[@id="textareawrapper"]/div/div[6]/div[1]/div/div/div/div[5]/pre[5]/span/span[4]',
)

print(left.text)


time.sleep(3)
browser.quit()
