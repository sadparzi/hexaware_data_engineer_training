import csv

with open("orders.csv", "r") as file:
    orders = list(csv.DictReader(file))


# Task 4
# Calculate Total Revenue

total_revenue = 0

for order in orders:
    revenue = int(order["quantity"]) * int(order["price"])
    total_revenue += revenue

print("Total Revenue =", total_revenue)


# Task 5
# Find Highest Order Value

highest_order_value = 0

for order in orders:
    revenue = int(order["quantity"]) * int(order["price"])

    if revenue > highest_order_value:
        highest_order_value = revenue

print("Highest Order Value =", highest_order_value)


# Task 6
# Find Lowest Order Value

lowest_order_value = float("inf")

for order in orders:
    revenue = int(order["quantity"]) * int(order["price"])

    if revenue < lowest_order_value:
        lowest_order_value = revenue

print("Lowest Order Value =", lowest_order_value)


# Task 7
# Find Average Order Value

total_revenue = 0

for order in orders:
    revenue = int(order["quantity"]) * int(order["price"])
    total_revenue += revenue

average_order_value = total_revenue / len(orders)

print("Average Order Value =", average_order_value)