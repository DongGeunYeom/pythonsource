# 저장하고 싶은 이미지
import urllib.request as req

url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSigYq1kqyDo4tAfLLwPkE3_px4Pmi4FFAuOw&usqp=CAU"
# 다운로드 받을 경로
path = "./rpabasic/crawl/download/"

try:
    file1, header1 = req.urlretrieve(url, path + "test.png")
except Exception as e:
    print(e)
else:
    print(header1)
    print("성공")
