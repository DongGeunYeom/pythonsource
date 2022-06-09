import urllib.request as req

# 이미지, html 파일 다운로드

target_url = [
    "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA2MDJfMTIy%2FMDAxNjU0MTU3NDg0MDg1.aXt_GhWmQIEdRvQUN1Nps13-xX4RC1JpDBbbf69ub8gg.hKmWBhtVcFiRJ4qXnRi4fd-K6T4chPGhRyTcZqrOUf0g.JPEG.theanimalpress%2F%25C0%25CE%25BD%25CE%25B0%25ED%25BE%25E7%25C0%25CC_%25281%2529.jpg&type=a340",
    "https://www.naver.com",
]

# 다운로드 받을 경로
path_list = [
    "./rpabasic/crawl/download/cat.png",
    "./rpabasic/crawl/download/naver.html",
]

for i, url in enumerate(target_url):
    try:
        res = req.urlopen(url)
        contents = res.read()

        print("------------------------------------")
        print("Header info-{} - {}".format(i, res.info()))
        print("http status : {}".format(res.getcode()))
        print("------------------------------------")

        with open(path_list[i], "wb") as c:
            c.write(contents)

    except Exception as e:
        print(e)
    else:
        print("성공")
