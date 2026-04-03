import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales_data.csv")

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Basic info
print("Dataset Info:")
print(df.info())

# Total sales by product
product_sales = df.groupby('Product')['Sales'].sum()
print("\nSales by Product:")
print(product_sales)

# Total sales by region
region_sales = df.groupby('Region')['Sales'].sum()
print("\nSales by Region:")
print(region_sales)

# Monthly sales trend
df['Month'] = df['Date'].dt.month
monthly_sales = df.groupby('Month')['Sales'].sum()

# --- Visualization ---

# Bar chart (Product vs Sales)
product_sales.plot(kind='bar')
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

# Line chart (Monthly Sales)
monthly_sales.plot(kind='line', marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
