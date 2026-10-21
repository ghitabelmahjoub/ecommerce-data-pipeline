import pandas as pd

file_path = "data/raw/Online Retail.xlsx"

df = pd.read_excel(file_path)

print("Dataset loaded successfully!")
print()
print("Shape:", df.shape)
print()
print("Columns:")
print(df.columns.tolist())
print()
print("First 5 rows:")
print(df.head())