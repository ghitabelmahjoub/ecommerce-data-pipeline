import sqlite3

db_path = "data/ecommerce.db"

conn = sqlite3.connect(db_path)

query = """
SELECT
    StockCode,
    Description,
    ROUND(AVG(UnitPrice), 2) AS average_price,
    SUM(Quantity) AS units_sold,
    ROUND(SUM(Quantity * UnitPrice), 2) AS revenue
FROM transactions
WHERE StockCode NOT IN ('DOT', 'POST', 'M')
GROUP BY StockCode, Description
HAVING units_sold > 100
ORDER BY average_price DESC
LIMIT 10;
"""

results = conn.execute(query).fetchall()

print("Top 10 Products by Average Price")
print("-" * 80)

for stock_code, description, avg_price, units_sold, revenue in results:
    print(
        f"{stock_code} | {description} | "
        f"Avg Price: £{avg_price:,.2f} | "
        f"Units: {units_sold:,} | "
        f"Revenue: £{revenue:,.2f}"
    )

conn.close()