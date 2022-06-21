# train.xlsx 읽어서 정규식 적용

from openpyxl import load_workbook
import re

from requests import patch

path = "./rpabasic/crawl/download/"

wb = load_workbook(path + "train.xlsx")
ws = wb.active

# Name 출력 - Potter, Mrs. Thomas Jr (Lily Alexenia Wilson), Shelley, Mrs. William (Imanita Parrish Hall)
pattern = re.compile(" [A-Za-z]+\.")
pattern3 = re.compile(" Miss\.")
pattern5 = re.compile(" Mrs\.")

# 남자 승객명 출력
pattern2 = re.compile(" Mr\.")
for x in ws.rows:
    if len(pattern.findall(x[3].value)) > 0:
        print(x[3].value)

    # print(pattern.search(x[3].value).group())
