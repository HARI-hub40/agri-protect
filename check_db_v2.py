import sqlite3
import os

db_path = r'd:\agri\backend\users.db'
if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    tables = ['users', 'history', 'finance', 'fields', 'disease_reports']
    for table in tables:
        print(f"--- {table} ---")
        try:
            c.execute(f"PRAGMA table_info({table});")
            for col in c.fetchall():
                print(col)
        except Exception as e:
            print(f"Error checking {table}: {e}")
    conn.close()
else:
    print("DB not found")
