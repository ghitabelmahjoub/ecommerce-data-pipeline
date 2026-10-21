CREATE TABLE IF NOT EXISTS transactions (
    InvoiceNo TEXT NOT NULL,
    StockCode TEXT NOT NULL,
    Description TEXT NOT NULL,
    Quantity INTEGER NOT NULL,
    InvoiceDate TEXT NOT NULL,
    UnitPrice REAL NOT NULL,
    CustomerID REAL,
    Country TEXT NOT NULL
);