import sqlite3
import os

import sqlite3
import os

db_path = 'instance/database.db'
if not os.path.exists(db_path):
    db_path = 'database.db'
    if not os.path.exists(db_path):
        print("database.db not found in root or instance/")
    else:
        conn = sqlite3.connect(db_path)
else:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Try different table names
    tables = ['user', 'users', 'User']
    for table in tables:
        try:
            cursor.execute(f"SELECT * FROM {table}")
            rows = cursor.fetchall()
            print(f"Table '{table}': {len(rows)} records")
            for row in rows:
                print(row)
            break
        except sqlite3.OperationalError:
            continue
    
    conn.close()
