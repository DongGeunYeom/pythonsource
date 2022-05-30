# data/word.txt 로드한 후 단어들 섞기
# 섞은 단어들 중에서 하나를 뽑아서 화면에 출력
# 출력된 단어를 보고 사용자는 똑같이 타이핑 하는 프로그램

import random
import time
import sqlite3
from datetime import datetime

conn = sqlite3.connect("data/records.db", isolation_level=None)
cursor = conn.cursor()
# 테이블 생성
sql = """
CREATE TABLE IF NOT EXISTS records
(id integer primary key autoincrement, cnt integer, record text, regdate text)
"""
cursor.execute(sql)


# data/word.txt 로드한 후 words 리스트에 단어들을 붙여넣기
words = []
with open("data/word.txt", "r", encoding="utf-8") as f:
    for n in f:
        words.append(n.strip())

count = 0
n = 1
input("Ready? Press Enter Key")
# 시작 시간
start = time.time()  # 초 단위 리턴(1970년 1월 1일 0시 0분 0초부터)

while n <= 5:
    # 리스트 속의 단어 섞기
    random.shuffle(words)
    # 임의의 단어 추출
    question = random.choice(words)

    print()

    print("Question #{}".format(n))
    print(question)
    # 사용자로부터 입력 받기
    x = input()

    # 사용자의 입력값과 문제가 일치하는지 확인
    # 일치한다면 Pass 글자 출력, 정답 개수 추가
    if question.strip() == x.strip():
        print("Pass!!")
        count += 1
    else:
        # 일치하지 않는다면 Wrong 출력
        print("Wrong...")

    n += 1

# 종료 시간
end = time.time()

# 게임하는 데 걸린 시간 출력
getTime = end - start
getTime = format(getTime, ".2f")
print("게임시간 : {}초, 정답개수 : {}개".format(getTime, count))

# 정답 개수가 4개 이상이면 합격, 아니면 불합격
if count >= 4:
    print("합격")
else:
    print("불합격")

# 기록 삽입(정답개수, 시간, 오늘날짜(2022-05-30 12:04:00))
today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

sql = "INSERT INTO records('cnt','record','regdate') VALUES(?,?,?)"
cursor.execute(sql, (count, getTime, today))
