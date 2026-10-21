import sqlite3
import pandas as pd

# File paths
csv_path = "data/processed/online_retail_cleaned.csv"
db_path = "data/ecommerce.db"

# Load cleaned CSV
df = pd.read_csv(csv_path, dtype={"InvoiceNo": str}, low_memory=False)
# Validate required columns
required_columns = [
    "InvoiceNo",
    "StockCode",
    "Quantity",
    "InvoiceDate",
    "UnitPrice",
    "Country"
]

missing_columns = [
    column for column in required_columns
    if column not in df.columns
]

if missing_columns:
    raise ValueError(
        f"Missing required columns: {missing_columns}"
    )

# Validate critical fields
if df["InvoiceNo"].isna().any():
    raise ValueError("InvoiceNo contains missing values.")

if df["StockCode"].isna().any():
    raise ValueError("StockCode contains missing values.")

if df["Quantity"].isna().any():
    raise ValueError("Quantity contains missing values.")

if df["UnitPrice"].isna().any():
    raise ValueError("UnitPrice contains missing values.")

print("Data validation passed!")
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