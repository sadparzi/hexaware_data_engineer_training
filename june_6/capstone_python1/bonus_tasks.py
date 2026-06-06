import csv

with open("orders.csv", "r") as file:
    orders = list(csv.DictReader(file))


# Task 38
# Generate high_value_orders.csv
# Orders Above ₹50,000

with open(
    "high_value_orders.csv",
    "w",
    newline=""
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=orders[0].keys()
    )

    writer.writeheader()

    for order in orders:
        revenue = (
            int(order["quantity"]) *
            int(order["price"])
        )

        if revenue > 50000:
            writer.writerow(order)


# Task 39
# Generate electronics_orders.csv
# Only Electronics Category

with open(
    "electronics_orders.csv",
    "w",
    newline=""
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=orders[0].keys()
    )

    writer.writeheader()

    for order in orders:
        if order["category"] == "Electronics":
            writer.writerow(order)


print("Files Generated Successfully")