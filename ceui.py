import sqlite3

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

c.execute("SELECT * FROM pad_shujuku WHERE 账号编号='B12'")
data = c.fetchone()

print(data[7])

# a=data[4].count('5489')
# print(a)