# 구글 뉴스 클리핑
import requests
from bs4 import BeautifulSoup


def main():
    url = "https://news.google.com/search?q=%ED%8C%8C%EC%9D%B4%EC%8D%AC&hl=ko&gl=KR&ceid=KR%3Ako"

    res = requests.get(url)
    soup = BeautifulSoup(res.text, "lxml")

    news_clipping = data_extract(soup)

    for section in news_clipping:
        for k, v in section.items():
            print("{} : {} ".format(k, v))
        print()


def data_extract(soup):
    # 원하는 요소 추출
    # [{href : "", title : ""},{},{}]
    news_list = []
    news_item = {}

    # 뉴스 원문 url, 제목, 출처, 등록 일시
    # 각 개별 기사는 dict 구조로 생성
    articles = soup.select("div.xrnccd > article")
    for article in articles:
        # print(article)
        # 제목과 링크를 가지고 있는 태그 요소 찾기
        link_title = article.select_one("h3 > a")

        base_url = "https://news.google.com"

        # ./articles/CBMin1293aisd ==? https://news.google.com/articles~~
        news_item["href"] = base_url + link_title["href"][1:]
        news_item["title"] = link_title.get_text()

        # 출처와 뉴스보도 시간을 가지고 있는 요소 찾기
        writer_time = article.select_one("div.SVJrMe")

        # 출처만 추출
        news_item["writer"] = writer_time.select_one("a").get_text()
        # 시간만 추출
        date_time = writer_time.select_one("time")

        if date_time:
            report_date_time = date_time["datetime"].split("T")
            news_item["report_date"] = report_date_time[0]
            news_item["report_time"] = report_date_time[1]
        else:
            news_item["report_date"] = ""
            news_item["report_time"] = ""

        news_list.append(news_item)
        news_item = {}

    # 리스트 리턴
    return news_list


if __name__ == "__main__":
    main()
