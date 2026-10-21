-- ==========================================
-- E-COMMERCE DATA PIPELINE
-- Analytics Queries
-- ==========================================


-- ==========================================
-- Query 1: Total Revenue
-- ==========================================

SELECT
    ROUND(SUM(Quantity * UnitPrice), 2) AS total_revenue
FROM transactions;


-- ==========================================
-- Query 2: Monthly Revenue
-- ==========================================

SELECT
    SUBSTR(InvoiceDate, 1, 7) AS month,
    ROUND(SUM(Quantity * UnitPrice), 2) AS revenue
FROM transactions
GROUP BY month
ORDER BY month;


-- ==========================================
-- Query 3: Top 10 Products by Revenue
-- ==========================================

SELECT
    StockCode,
    Description,
    ROUND(SUM(Quantity * UnitPrice), 2) AS revenue
FROM transactions
WHERE StockCode NOT IN ('DOT', 'POST', 'M')
GROUP BY StockCode, Description
ORDER BY revenue DESC
LIMIT 10;


-- ==========================================
-- Query 4: Revenue by Country
-- ==========================================

SELECT
    Country,
    ROUND(SUM(Quantity * UnitPrice), 2) AS revenue
FROM transactions
GROUP BY Country
ORDER BY revenue DESC;


-- ==========================================
-- Query 5: Top 10 Customers by Revenue
-- ==========================================

SELECT
    CustomerID,
    ROUND(SUM(Quantity * UnitPrice), 2) AS revenue
FROM transactions
WHERE CustomerID IS NOT NULL
GROUP BY CustomerID
ORDER BY revenue DESC
LIMIT 10;


-- ==========================================
-- Query 6: Number of Orders by Country
-- ==========================================

SELECT
    Country,
    COUNT(DISTINCT InvoiceNo) AS orders
FROM transactions
GROUP BY Country
ORDER BY orders DESC;


-- ==========================================
-- Query 7: Average Order Value
-- ==========================================

SELECT
    ROUND(
        SUM(Quantity * UnitPrice) / COUNT(DISTINCT InvoiceNo),
        2
    ) AS average_order_value
FROM transactions;


-- ==========================================
-- Query 8: Top 10 Products by Units Sold
-- ==========================================

SELECT
    StockCode,
    Description,
    SUM(Quantity) AS units_sold
FROM transactions
WHERE StockCode NOT IN ('DOT', 'POST', 'M')
GROUP BY StockCode, Description
ORDER BY units_sold DESC
LIMIT 10;


-- ==========================================
-- Query 9: Top 10 Products by Average Price
-- ==========================================

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