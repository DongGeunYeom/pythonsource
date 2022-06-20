# 다나와 로그인

import requests
from bs4 import BeautifulSoup

# 요청
login_info = {
    "redirectUrl": "http://www.danawa.com/",
    "loginMemberType": "general",
    "id": "meronot1",
    "isSaveId": "true",
    "password": "rptksqud1%",
}

# 헤더정보
headers = {
    "Referer": "https://auth.danawa.com/login?url=http%3A%2F%2Fwww.danawa.com%2F",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0",
}

# 세션을 이용한 작업
with requests.Session() as s:

    # 로그인
    res = s.post("https://auth.danawa.com/login", login_info, headers=headers)

    # 주문 /배송 조회
    res = s.get("https://buyer.danawa.com/order/Order/orderList", headers=headers)

    # 현재 페이지 파싱
    soup = BeautifulSoup(res.text, "lxml")

    # 아이디 찾기
    user_id = soup.find("p", class_="user")
    print(user_id, user_id.get_text())
    if user_id is None:
        raise Exception("Login 실패, 아이디나 비밀번호 확인")

    # 상단메뉴 가져오기
    menu_list = soup.select("div > ul.info_list > li")

    for menu in menu_list:
        # 메뉴명, 수량
        proc, val = (
            menu.find("span").get_text().strip(),
            menu.find("strong").get_text().strip(),
        )
        print(f"{proc}:{val}")
