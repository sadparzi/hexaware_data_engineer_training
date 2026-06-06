#part 1 file handling 

import csv

with open("orders.csv", "r") as file:
    orders = list(csv.DictReader(file))


# Task 1
# Read orders.csv

print(orders)


# Task 2
# Display all records

for order in orders:
    print(order)


# Task 3
# Count total orders

print("Total Orders =", len(orders))