cities = ("Hyderabad", "Mumbai", "Delhi", "Chennai", "Pune")  # Tuple

print(cities)

print(cities[0])
print(cities[1])

print(cities[-1])
print(cities[-2])

print(len(cities))

print(cities[1:4])

cities[1] = "Bangalore" # This will raise an error because tuples are immutable