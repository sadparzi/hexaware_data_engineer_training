import csv

with open("orders.csv", "r") as file:
    orders = list(csv.DictReader(file))


# Task 11
# Count Orders By Product

product_count = {}

for order in orders:
    product = order["product"]

    if product in product_count:
        product_count[product] += 1
    else:
        product_count[product] = 1

print(product_count)


# Task 12
# Calculate Revenue By Product

product_revenue = {}

for order in orders:
    product = order["product"]
    revenue = int(order["quantity"]) * int(order["price"])

    if product in product_revenue:
        product_revenue[product] += revenue
    else:
        product_revenue[product] = revenue

print(product_revenue)


# Task 13
# Find Most Sold Product

product_quantity = {}

for order in orders:
    product = order["product"]
    quantity = int(order["quantity"])

    if product in product_quantity:
        product_quantity[product] += quantity
    else:
        product_quantity[product] = quantity

most_sold_product = max(
    product_quantity,
    key=product_quantity.get
)

print("Most Sold Product =", most_sold_product)
print("Quantity Sold =", product_quantity[most_sold_product])


# Task 14
# Find Least Sold Product

product_quantity = {}

for order in orders:
    product = order["product"]
    quantity = int(order["quantity"])

    if product in product_quantity:
        product_quantity[product] += quantity
    else:
        product_quantity[product] = quantity

least_sold_product = min(
    product_quantity,
    key=product_quantity.get
)

print("Least Sold Product =", least_sold_product)
print("Quantity Sold =", product_quantity[least_sold_product])


# Task 15
# Calculate Revenue By Category

category_revenue = {}

for order in orders:
    category = order["category"]
    revenue = int(order["quantity"]) * int(order["price"])

    if category in category_revenue:
        category_revenue[category] += revenue
    else:
        category_revenue[category] = revenue

print(category_revenue)