cities = ["Hyderabad", "Mumbai", "Delhi"]
#indexing
print(cities[0])
print(cities[1])
print(cities[2])
#negative indexing
print(cities[-1])
print(cities[-2])

#updating list
cities[1] = "Bangalore"
print(cities)

#appending to list
cities.append("Chennai")
print(cities)

#inserting to list
cities.insert(1, "Pune")
print(cities)

#adding multiple items to list
cities.extend(["Kochi", "Pondi"])
print(cities)

#removing items from list
cities.remove("Mumbai")
print(cities)

cities.pop(1)
print(cities)

del cities[0]
print(cities)

cities.clear()
print(cities)

print(len(cities))

# Check Membership
print("Mumbai" in cities)
print("Pune" in cities)

print(cities.index("Mumbai"))

cities.sort()
print(cities)

