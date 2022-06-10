from urllib.request import urlopen, Request
from fake_useragent import UserAgent

url = "https://www.edaily.co.kr/news/read?newsId=01252966632360408&mediaCodeNo=257&OutLnkChk=Y"

try:
    userAgent = UserAgent()
    headers = {"user-agent": userAgent.chrome}
    request_url = Request(url, headers=headers)
    res = urlopen(request_url).read().decode("utf-8")
    # print(res)
    print(
        request_url.header_items()
    )  # [('Host', 'www.edaily.co.kr'), ('User-agent', 'Python-urllib/3.10')]
except:
    print("error")
