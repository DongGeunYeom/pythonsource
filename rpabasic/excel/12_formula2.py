# 함수 삽입
from datetime import datetime
from openpyxl import load_workbook

wb = load_workbook("./rpabasic/excel/formula.xlsx", data_only=True)
ws = wb.active

for row in ws.values:
    for cell in row:
        print(cell)
