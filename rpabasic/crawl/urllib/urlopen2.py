# request - 2) urlopen() : 다운로드는 하지 않고 정보를 메모리에 올려서 분석
#                 read() :

import urllib.request as req

try:
    url = "https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&xfrom=main^gnb"
    res = req.urlopen(url)
    content = res.read().decode("euc-kr")

except Exception as e:
    print(e)
else:
    print(content[:3000])
    print(res.info())
