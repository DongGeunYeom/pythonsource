# db 연동
# SQLite : 내장 DB, python, spring boot
import sqlite3
from datetime import datetime

# print(sqlite3.version)
# print(sqlite3.sqlite_version)

# # 날짜 생성
now = datetime.now()

# print("now ", now)
now_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
# print("now_date_time ",now_date_time)

# 데이터베이스 생성
conn = sqlite3.connect("data/database.db", isolation_level=None)

# 커서 (Cursor)
cursor = conn.cursor()
print(type(cursor))

# 테이블 생성
cursor.execute(
    "CREATE TABLE IF NOT EXISTS users(id integer primary key, username text, phone text, website text, regdate text)"
)

# insert

# cursor.execute(
#     "INSERT INTO users VALUES(1, 'Kim', '010-1234-1234', 'kim.com', ?)",
#     (now_date_time,),
# )

# cursor.execute(
#     "INSERT INTO users VALUES(?,?,?,?,?)",
#     (2, "hong", "010-1234-4567", "hong.com", now_date_time),
# )

# 여러개 삽입
user_list = (
    (6, "park", "010-4567-1234", "park.com", now_date_time),
    (7, "choi", "010-9876-1234", "choi.com", now_date_time),
    (8, "yoo", "010-3687-1234", "yoo.com", now_date_time),
)

cursor.executemany("INSERT INTO users VALUES(?,?,?,?,?)", user_list)
