import sqlite3
import pandas as pd

# File paths
csv_path = "data/processed/online_retail_cleaned.csv"
db_path = "data/ecommerce.db"

# Load cleaned CSV
df = pd.read_csv(csv_path)

# Connect to SQLite database
conn = sqlite3.connect(db_path)

# Load data into transactions table
df.to_sql(
    "transactions",
    conn,
    if_exists="replace",
    index=False
)

# Close connection
conn.close()

print("Data loaded successfully!")
print("Rows loaded:", len(df))