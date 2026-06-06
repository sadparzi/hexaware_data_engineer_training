import csv

with open("orders.csv", "r") as file:
    orders = list(csv.DictReader(file))


# Task 8
# Display All Unique Customers

customers = set()

for order in orders:
    customers.add(order["customer_name"])

for customer in customers:
    print(customer)


# Task 9
# Count Unique Customers

customers = set()

for order in orders:
    customers.add(order["customer_name"])

print("Unique Customers =", len(customers))


# Task 10
# Find Customer With Highest Purchase Amount

customer_revenue = {}

for order in orders:
    customer = order["customer_name"]
    revenue = int(order["quantity"]) * int(order["price"])

    if customer in customer_revenue:
        customer_revenue[customer] += revenue
    else:
        customer_revenue[customer] = revenue

top_customer = max(
    customer_revenue,
    key=customer_revenue.get
)

print("Customer =", top_customer)
print("Purchase Amount =", customer_revenue[top_customer])