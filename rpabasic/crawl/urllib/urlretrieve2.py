import urllib.request as req

# 이미지, html 파일 다운로드

img_url = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA2MDJfMTIy%2FMDAxNjU0MTU3NDg0MDg1.aXt_GhWmQIEdRvQUN1Nps13-xX4RC1JpDBbbf69ub8gg.hKmWBhtVcFiRJ4qXnRi4fd-K6T4chPGhRyTcZqrOUf0g.JPEG.theanimalpress%2F%25C0%25CE%25BD%25CE%25B0%25ED%25BE%25E7%25C0%25CC_%25281%2529.jpg&type=a340"
file_url = "https://www.naver.com"

# 다운로드 받을 경로
path = "./rpabasic/crawl/download/"

try:
    file1, header1 = req.urlretrieve(img_url, path + "cat.png")
    file2, header2 = req.urlretrieve(file_url, path + "naver.html")
except Exception as e:
    print(e)
else:
    print(header1)
    print()
    print(header2)
