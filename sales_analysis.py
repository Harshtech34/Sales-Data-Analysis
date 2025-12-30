"""
Sales Data Analysis Project
Author: Harshal Chavan
Description: Analyze sales data to extract insights such as total revenue,
best-selling product, and regional performance.
"""

import pandas as pd

# -----------------------------
# Day 1: Load Data
# -----------------------------
df = pd.read_csv("sales_data.csv")

# -----------------------------
# Day 2: Explore Data
# -----------------------------
print("Dataset Shape:", df.shape)
print("\nColumns:\n", df.columns)
print("\nData Types:\n", df.dtypes)

# -----------------------------
# Day 3: Clean Data
# -----------------------------

# Check missing values
print("\nMissing Values:\n", df.isnull().sum())

# Fill missing numeric values with 0 (if any)
df.fillna(0, inplace=True)

# Remove duplicate records
df.drop_duplicates(inplace=True)

# -----------------------------
# Day 4: Analyze Sales
# -----------------------------

# Metric 1: Total Revenue
total_revenue = df["Total_Sales"].sum()

# Metric 2: Best-Selling Product (by revenue)
best_product = df.groupby("Product")["Total_Sales"].sum().idxmax()

# Metric 3: Highest Revenue Region
best_region = df.groupby("Region")["Total_Sales"].sum().idxmax()

# Additional Metrics
total_orders = len(df)
average_order_value = df["Total_Sales"].mean()

# -----------------------------
# Day 5: Create Report
# -----------------------------
print("\n📊 SALES ANALYSIS REPORT")
print("-" * 30)
print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Best-Selling Product: {best_product}")
print(f"Top Revenue Region: {best_region}")
print(f"Total Orders: {total_orders}")
print(f"Average Order Value: ₹{average_order_value:,.2f}")

print("\nAnalysis Completed Successfully ✅")
