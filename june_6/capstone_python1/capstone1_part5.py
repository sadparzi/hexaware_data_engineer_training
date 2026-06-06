import csv

with open("orders.csv", "r") as file:
    orders = list(csv.DictReader(file))


# Task 16
# Count Orders By City

city_count = {}

for order in orders:
    city = order["city"]

    if city in city_count:
        city_count[city] += 1
    else:
        city_count[city] = 1

print(city_count)


# Task 17
# Calculate Revenue By City

city_revenue = {}

for order in orders:
    city = order["city"]
    revenue = int(order["quantity"]) * int(order["price"])

    if city in city_revenue:
        city_revenue[city] += revenue
    else:
        city_revenue[city] = revenue

print(city_revenue)


# Task 18
# Find City Generating Highest Revenue

city_revenue = {}

for order in orders:
    city = order["city"]
    revenue = int(order["quantity"]) * int(order["price"])

    if city in city_revenue:
        city_revenue[city] += revenue
    else:
        city_revenue[city] = revenue

top_city = max(
    city_revenue,
    key=city_revenue.get
)

print("Top City =", top_city)
print("Revenue =", city_revenue[top_city])