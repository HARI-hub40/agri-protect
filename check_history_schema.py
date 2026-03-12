import sqlite3
import os

db_path = r'd:\agri\backend\users.db'
conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute("PRAGMA table_info(history);")
print(c.fetchall())
conn.close()
