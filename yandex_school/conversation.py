import sqlite3
import sys

stdin = sys.stdin
conn = sqlite3.connect("conversations.db")
cursor = conn.cursor()
condition_1 = "author = 'Silver'"
condition_2 = "level_of_trust BETWEEN 6 AND 15"
order_column = "id"
query = f"SELECT condition FROM Talks WHERE {condition_1} AND {condition_2} ORDER BY {order_column}"
cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    print(row[0])
