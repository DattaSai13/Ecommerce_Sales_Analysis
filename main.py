# Week 4: Complete Data Analysis & Visualization Project
# Project: E-commerce Sales Analysis
# This program loads, cleans, analyzes, and visualizes sales data

import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------
# Load Data
# ----------------------------
df = pd.read_csv("sales_data.csv")

# Convert Date column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# ----------------------------
# Data Cleaning
# ----------------------------
df.fillna(0, inplace=True)      # Handle missing values
df.drop_duplicates(inplace=True)

# ----------------------------
# Data Analysis
# ----------------------------
total_revenue = df["Total_Sales"].sum()

sales_by_product = df.groupby("Product")["Total_Sales"].sum()
sales_by_region = df.groupby("Region")["Total_Sales"].sum()
monthly_sales = df.groupby(df["Date"].dt.month)["Total_Sales"].sum()

print("📊 E-COMMERCE SALES REPORT")
print("--------------------------------")
print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Best Selling Product: {sales_by_product.idxmax()}")
print(f"Top Performing Region: {sales_by_region.idxmax()}")
print("--------------------------------")

# ----------------------------
# Visualization 1: Bar Chart
# ----------------------------
plt.figure()
sales_by_product.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("visualizations/sales_by_product.png")
plt.show()

# ----------------------------
# Visualization 2: Line Chart
# ----------------------------
plt.figure()
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("visualizations/monthly_sales_trend.png")
plt.show()

# ----------------------------
# Visualization 3: Pie Chart
# ----------------------------
plt.figure()
sales_by_region.plot(kind="pie", autopct="%1.1f%%")
plt.title("Sales Distribution by Region")
plt.ylabel("")
plt.tight_layout()
plt.savefig("visualizations/sales_by_region.png")
plt.show()
