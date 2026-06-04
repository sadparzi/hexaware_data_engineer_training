customer = {
    "customer_id": 101,
    "name": "Rahul",
    "city": "Hyderabad"
}  # Dictionary

print(customer)

print(customer["name"])
print(customer["city"])

# Safe Access
print(customer.get("name"))
print(customer.get("salary"))

# Add New Key-Value Pair
customer["salary"] = 75000
print(customer)

# Update
customer["name"] = "Rahul Sharma"
print(customer)

customer.pop("salary")
print(customer)

del customer["salary"]