import csv

with open("orders.csv", "r") as file:
    orders = list(csv.DictReader(file))


# Task 19
# Store All Product Names In A List And Sort Alphabetically

products = []

for order in orders:
    products.append(order["product"])

products.sort()

print(products)


# Task 20
# Store Unique Cities In A Set And Display All Cities

cities = set()

for order in orders:
    cities.add(order["city"])

for city in cities:
    print(city)


# Task 21
# Create Dictionary {city : revenue}

city_revenue = {}

for order in orders:
    city = order["city"]
    revenue = int(order["quantity"]) * int(order["price"])

    if city in city_revenue:
        city_revenue[city] += revenue
    else:
        city_revenue[city] = revenue

print(city_revenue)


# Task 22
# Create Dictionary {product : quantity_sold}

product_quantity = {}

for order in orders:
    product = order["product"]
    quantity = int(order["quantity"])

    if product in product_quantity:
        product_quantity[product] += quantity
    else:
        product_quantity[product] = quantity

print(product_quantity)