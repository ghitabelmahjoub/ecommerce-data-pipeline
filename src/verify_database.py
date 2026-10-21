import sqlite3

db_path = "data/ecommerce.db"

conn = sqlite3.connect(db_path)

cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM transactions")

row_count = cursor.fetchone()[0]

print("Rows in database:", row_count)

conn.close()