set1 = {"Python", "SQL"}
set2 = {"MongoDB", "Python"}

result = set1.union(set2)
print(result)

result = set1.intersection(set2)
print(result)

result = set2.difference(set1)
print(result)

result = set1.symmetric_difference(set2) # non common values
print(result)