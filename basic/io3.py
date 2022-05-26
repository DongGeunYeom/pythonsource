# csv 파일 입출력
import csv

# with open("data/sample1.csv","r") as f:
#     reader = csv.reader(f)
#     # 헤더명 제거
#     next(reader)

#     print(reader)
#     print(type(reader))
#     print(dir(reader))
#     print()

#     for c in reader:
#         print(c)

# with open("data/sample2.csv","r") as f:

#     reader = csv.reader(f, delimiter="|")

#     for c in reader:
#         print(c)

# csv ==> dict 형태로 읽어오기
# with open("data/sample1.csv","r") as f:
#     reader = csv.DictReader(f)

#     for c in reader:
#         print(c) # {'번호': '10', '이름': '장혁철', '가입일시': '2017-12-01 13:01:11', '나이': '16'}
#         for k, v in c.items():
#             print(k,v)
#         print()

# sample3 읽기
# with open("data/sample3.csv","r") as f:
#     reader = csv.reader(f)

#     for c in reader:
#         print(c)

# 1차원 리스트 csv 파일로 저장
# list1 = list(range(1,6)) # list = [1,2,3,4,5]
# with open("data/sample4.csv","w") as f:
#     wt = csv.writer(f)

#     wt.writerow(list1)

# 2차원 리스트 csv 파일로 저장
# list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
# with open("data/sample5.csv","w", newline="") as f:
#     wt = csv.writer(f)
##    wt.writerows(list1)

#     for row in list1:
#         wt.writerow(row)


