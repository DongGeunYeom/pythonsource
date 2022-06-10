import requests
from fake_useragent import UserAgent

headers = {"user-agent": UserAgent().chrome}

# 순위, 제품명

try:
    url = "https://shoppinghow.kakao.com/siso/p/api/bestRank/dispprodbest?vCateId=GMP&durationDays=30&count=100&_=1654833631411"
    res = requests.get(url)

    rank_json = res.json()
    for idx, item in enumerate(rank_json, 1):
        print("순위 {}, 제품명 {} ".format(idx, item["product_name"]))


except Exception as e:
    print(e)
