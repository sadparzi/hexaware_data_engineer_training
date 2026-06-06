import pandas as pd


# Task 31
# Read CSV Using Pandas

df = pd.read_csv("orders.csv")

print(df)


# Task 32
# Create Revenue Column

df["Revenue"] = df["quantity"] * df["price"]

print(df)


# Task 33
# Display Top 5 Highest Value Orders

top_5_orders = df.sort_values(
    by="Revenue",
    ascending=False
).head(5)

print(top_5_orders)


# Task 34
# Group By City And Calculate Revenue

city_revenue = df.groupby(
    "city"
)["Revenue"].sum()

print(city_revenue)


# Task 35
# Group By Product And Calculate Revenue

product_revenue = df.groupby(
    "product"
)["Revenue"].sum()

print(product_revenue)


# Task 36
# Display Top Selling Products

top_products = df.groupby(
    "product"
)["quantity"].sum().sort_values(
    ascending=False
)

print(top_products)


# Task 37
# Display City-Wise Order Count

city_order_count = df.groupby(
    "city"
)["order_id"].count()

print(city_order_count)