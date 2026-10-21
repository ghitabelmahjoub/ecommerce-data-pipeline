import sqlite3
import pandas as pd

db_path = "data/ecommerce.db"

conn = sqlite3.connect(db_path)

queries = {

    "monthly_revenue": """
        SELECT
            SUBSTR(InvoiceDate, 1, 7) AS month,
            ROUND(SUM(Quantity * UnitPrice), 2) AS revenue
        FROM transactions
        GROUP BY month
        ORDER BY month;
    """,

    "country_revenue": """
        SELECT
            Country,
            ROUND(SUM(Quantity * UnitPrice), 2) AS revenue
        FROM transactions
        GROUP BY Country
        ORDER BY revenue DESC;
    """,

    "top_products_revenue": """
        SELECT
            StockCode,
            Description,
            ROUND(SUM(Quantity * UnitPrice), 2) AS revenue
        FROM transactions
        WHERE StockCode NOT IN ('DOT', 'POST', 'M')
        GROUP BY StockCode, Description
        ORDER BY revenue DESC
        LIMIT 10;
    """,

    "top_products_quantity": """
        SELECT
            StockCode,
            Description,
            SUM(Quantity) AS units_sold
        FROM transactions
        WHERE StockCode NOT IN ('DOT', 'POST', 'M')
        GROUP BY StockCode, Description
        ORDER BY units_sold DESC
        LIMIT 10;
    """,

    "top_customers": """
        SELECT
            CustomerID,
            ROUND(SUM(Quantity * UnitPrice), 2) AS revenue
        FROM transactions
        WHERE CustomerID IS NOT NULL
        GROUP BY CustomerID
        ORDER BY revenue DESC
        LIMIT 10;
    """,

    "orders_by_country": """
        SELECT
            Country,
            COUNT(DISTINCT InvoiceNo) AS orders
        FROM transactions
        GROUP BY Country
        ORDER BY orders DESC;
    """
}

for name, query in queries.items():

    df = pd.read_sql_query(query, conn)

    output_path = f"dashboard/data/{name}.csv"

    df.to_csv(output_path, index=False)

    print(f"{name}.csv → {len(df)} rows")

conn.close()

print("\nAll dashboard datasets exported successfully!")