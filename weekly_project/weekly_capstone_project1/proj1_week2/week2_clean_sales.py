"""
Retail Sales Performance Dashboard - Week 2
Data Collection & Cleanup Using Python (Pandas, NumPy)
"""

import pandas as pd
import numpy as np

# ============================================================
# Load Data
# ============================================================

df = pd.read_csv('sales.csv')

print("=== Raw Data Info ===")
print(df.info())
print()
print("=== Raw Data Preview ===")
print(df.head(10))
print()
print("=== Missing Values per Column ===")
print(df.isnull().sum())
print()

# ============================================================
# Clean Missing Values
# ============================================================

# quantity: missing -> fill with median quantity (robust to outliers)
median_qty = df['quantity'].median()
df['quantity'] = df['quantity'].fillna(median_qty)

# price: missing -> fill with mean price per product_id (fallback to overall mean)
df['price'] = df.groupby('product_id')['price'].transform(
    lambda x: x.fillna(x.mean())
)
df['price'] = df['price'].fillna(df['price'].mean())

# cost: missing -> fill with mean cost per product_id (fallback to overall mean)
df['cost'] = df.groupby('product_id')['cost'].transform(
    lambda x: x.fillna(x.mean())
)
df['cost'] = df['cost'].fillna(df['cost'].mean())

# discount_pct: missing -> assume no discount
df['discount_pct'] = df['discount_pct'].fillna(0)

# sale_date: missing -> drop those rows (can't analyze trends without a date)
df = df.dropna(subset=['sale_date'])

# ============================================================
# Correct Data Types
# ============================================================

df['quantity'] = df['quantity'].astype(int)
df['sale_date'] = pd.to_datetime(df['sale_date'])
df['store_id'] = df['store_id'].astype(int)
df['product_id'] = df['product_id'].astype(int)

# ============================================================
# Fix Invalid Data (negative quantity is impossible -> take absolute value)
# ============================================================

invalid_qty_count = (df['quantity'] < 0).sum()
print(f"Found {invalid_qty_count} rows with negative quantity — correcting using abs()")
df['quantity'] = np.abs(df['quantity'])

print()
print("=== Cleaned Data Info ===")
print(df.info())
print()
print("=== Missing Values After Cleanup ===")
print(df.isnull().sum())
print()

# ============================================================
# Calculate Revenue, Discount, Profit Margins using NumPy
# ============================================================

df['revenue'] = np.round(df['quantity'] * df['price'] * (1 - df['discount_pct'] / 100), 2)
df['total_cost'] = np.round(df['quantity'] * df['cost'], 2)
df['profit'] = np.round(df['revenue'] - df['total_cost'], 2)
df['profit_margin_pct'] = np.round((df['profit'] / df['revenue']) * 100, 2)

print("=== Data with Calculated Fields ===")
print(df.head(10))
print()

# ============================================================
# Summary: Total Revenue and Profit by Store
# ============================================================

summary_by_store = df.groupby('store_id')[['revenue', 'profit']].sum().round(2)
summary_by_store = summary_by_store.sort_values('revenue', ascending=False)

print("=== Summary: Revenue & Profit by Store ===")
print(summary_by_store)
print()

# ============================================================
# Summary: Total Revenue and Profit by Product
# ============================================================

summary_by_product = df.groupby('product_id')[['revenue', 'profit']].sum().round(2)
summary_by_product = summary_by_product.sort_values('revenue', ascending=False)

print("=== Summary: Revenue & Profit by Product ===")
print(summary_by_product)
print()

# ============================================================
# Overall Summary Stats
# ============================================================

print("=== Overall Summary ===")
print(f"Total Revenue: {df['revenue'].sum():,.2f}")
print(f"Total Profit: {df['profit'].sum():,.2f}")
print(f"Average Profit Margin: {df['profit_margin_pct'].mean():.2f}%")
print(f"Total Units Sold: {df['quantity'].sum()}")

# ============================================================
# Save Cleaned Dataset
# ============================================================

df.to_csv('sales_cleaned.csv', index=False)
print()
print("Cleaned dataset saved as sales_cleaned.csv")
