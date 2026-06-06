import csv

with open("orders.csv", "r") as file:
    orders = list(csv.DictReader(file))


# Task 23
# calculate_total_revenue()

def calculate_total_revenue():
    total_revenue = 0

    for order in orders:
        revenue = int(order["quantity"]) * int(order["price"])
        total_revenue += revenue

    return total_revenue


print("Total Revenue =", calculate_total_revenue())


# Task 24
# find_top_product()

def find_top_product():
    product_quantity = {}

    for order in orders:
        product = order["product"]
        quantity = int(order["quantity"])

        if product in product_quantity:
            product_quantity[product] += quantity
        else:
            product_quantity[product] = quantity

    return max(product_quantity, key=product_quantity.get)


print("Top Product =", find_top_product())


# Task 25
# find_top_city()

def find_top_city():
    city_revenue = {}

    for order in orders:
        city = order["city"]
        revenue = int(order["quantity"]) * int(order["price"])

        if city in city_revenue:
            city_revenue[city] += revenue
        else:
            city_revenue[city] = revenue

    return max(city_revenue, key=city_revenue.get)


print("Top City =", find_top_city())


# Task 26
# find_average_order_value()

def find_average_order_value():
    total_revenue = 0

    for order in orders:
        revenue = int(order["quantity"]) * int(order["price"])
        total_revenue += revenue

    return total_revenue / len(orders)


print("Average Order Value =", find_average_order_value())