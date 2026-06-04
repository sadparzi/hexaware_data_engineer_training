cities = {"Hyderabad", "Mumbai", "Delhi"}  # Set

print(cities)

cities = {"Hyderabad", "Mumbai", "Delhi", "Mumbai"}
print(cities)

# Remove Duplicates from List
# cities = ["Hyderabad", "Mumbai", "Mumbai", "Delhi"]
# unique_cities = set(cities)
# print(unique_cities)

cities.add("Chennai")
print(cities)

cities.update(["Delhi", "Pune"])
print(cities)

cities.remove("Mumbai")
print(cities)

cities.discard("Pune")  # No Error when data is not present
print(cities)