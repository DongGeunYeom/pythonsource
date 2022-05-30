import sqlite3

conn = sqlite3.connect("data/database.db", isolation_level=None)

cursor = conn.cursor()

# 조회
# sql = """select *
# from users
# """

# cursor.execute(sql)

# fetchon(), fetchmany(), fetchall()
# print("1 ",cursor.fetchone()) # select 결과로 나온 제일 첫 번째 행
# print("3, ", cursor.fetchmany(size=3))
# print("3 ", cursor.fetchall())

# for row in cursor.fetchall():
#     print("rows ",row)

# sql = """select *
# from users order by id desc
# """

# cursor.execute(sql)

# for row in cursor.fetchall():
#     print("rows ",row)


# sql = """select *
# from users where id = ?
# """

# cursor.execute(sql, (3,))

# for row in cursor.fetchall():
#     print("rows ",row)


# sql = """select *
# from users where id = %s
# """

# param = 4
# cursor.execute(sql % param)

# for row in cursor.fetchall():
#     print("rows ",row)


# sql = """select *
# from users where id = :id
# """

# cursor.execute(sql, {"id": 5})

# for row in cursor.fetchall():
#     print("rows ", row)


sql = """select *
from users where id in (?,?)
"""

param = (3, 6)
cursor.execute(sql, param)

for row in cursor.fetchall():
    print("rows ", row)
