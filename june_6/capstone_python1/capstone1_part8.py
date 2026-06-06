import csv


# Task 27
# Handle Missing CSV File

try:
    with open("orders.csv", "r") as file:
        orders = list(csv.DictReader(file))

    print("File Loaded Successfully")

except FileNotFoundError:
    print("orders.csv file not found")


# Task 28
# Handle Invalid Quantity Values

try:
    with open("orders.csv", "r") as file:
        orders = list(csv.DictReader(file))

    total_revenue = 0

    for order in orders:
        quantity = int(order["quantity"])
        price = int(order["price"])

        total_revenue += quantity * price

    print("Total Revenue =", total_revenue)

except ValueError:
    print("Invalid Quantity Value Found")


# Task 29
# Handle Invalid Price Values

try:
    with open("orders.csv", "r") as file:
        orders = list(csv.DictReader(file))

    total_revenue = 0

    for order in orders:
        quantity = int(order["quantity"])
        price = int(order["price"])

        total_revenue += quantity * price

    print("Total Revenue =", total_revenue)

except ValueError:
    print("Invalid Price Value Found")