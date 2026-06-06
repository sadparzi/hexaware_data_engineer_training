import csv
import numpy as np

with open("orders.csv", "r") as file:
    orders = list(csv.DictReader(file))


# Task 30
# Create NumPy Array Containing Order Values

order_values = []

for order in orders:
    revenue = int(order["quantity"]) * int(order["price"])
    order_values.append(revenue)

order_values = np.array(order_values)

print("Order Values =", order_values)

print("Total Revenue =", np.sum(order_values))

print("Average Revenue =", np.mean(order_values))

print("Maximum Revenue =", np.max(order_values))

print("Minimum Revenue =", np.min(order_values))

print("Standard Deviation =", np.std(order_values))