import csv

with open("orders.csv", "r") as file:
    orders = list(csv.DictReader(file))


# Total Orders

total_orders = len(orders)


# Total Revenue

total_revenue = 0

for order in orders:
    total_revenue += (
        int(order["quantity"]) *
        int(order["price"])
    )


# Average Order Value

average_order_value = (
    total_revenue / total_orders
)


# Highest Order Value

highest_order_value = 0

for order in orders:
    revenue = (
        int(order["quantity"]) *
        int(order["price"])
    )

    if revenue > highest_order_value:
        highest_order_value = revenue


# Lowest Order Value

lowest_order_value = float("inf")

for order in orders:
    revenue = (
        int(order["quantity"]) *
        int(order["price"])
    )

    if revenue < lowest_order_value:
        lowest_order_value = revenue


# Revenue By City

city_revenue = {}

for order in orders:
    city = order["city"]

    revenue = (
        int(order["quantity"]) *
        int(order["price"])
    )

    if city in city_revenue:
        city_revenue[city] += revenue
    else:
        city_revenue[city] = revenue


# Revenue By Category

category_revenue = {}

for order in orders:
    category = order["category"]

    revenue = (
        int(order["quantity"]) *
        int(order["price"])
    )

    if category in category_revenue:
        category_revenue[category] += revenue
    else:
        category_revenue[category] = revenue


# Top Selling Product

product_quantity = {}

for order in orders:
    product = order["product"]

    if product in product_quantity:
        product_quantity[product] += int(order["quantity"])
    else:
        product_quantity[product] = int(order["quantity"])

top_product = max(
    product_quantity,
    key=product_quantity.get
)


# Top Revenue Generating City

top_city = max(
    city_revenue,
    key=city_revenue.get
)


# Generate sales_summary_report.txt

with open(
    "sales_summary_report.txt",
    "w"
) as report:

    report.write(
        f"Total Orders = {total_orders}\n"
    )

    report.write(
        f"Total Revenue = {total_revenue}\n"
    )

    report.write(
        f"Average Order Value = {average_order_value}\n"
    )

    report.write(
        f"Highest Order Value = {highest_order_value}\n"
    )

    report.write(
        f"Lowest Order Value = {lowest_order_value}\n\n"
    )

    report.write(
        "Revenue By City\n"
    )

    for city, revenue in city_revenue.items():
        report.write(
            f"{city} = {revenue}\n"
        )

    report.write("\n")

    report.write(
        "Revenue By Category\n"
    )

    for category, revenue in category_revenue.items():
        report.write(
            f"{category} = {revenue}\n"
        )

    report.write("\n")

    report.write(
        f"Top Selling Product = {top_product}\n"
    )

    report.write(
        f"Top Revenue Generating City = {top_city}\n"
    )

print("sales_summary_report.txt generated successfully")