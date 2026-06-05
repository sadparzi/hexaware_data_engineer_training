import csv

with open(
    "employees.csv",
    "r"
) as file:

    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        print(row)

    for row in reader:
        print(row[1])  # Print employee names 

#count number of employees
with open(
    "employees.csv",
    "r"
) as file:

    reader = csv.reader(file)
    next(reader)  # Skip header row
    count = 0
    for row in reader:
        count += 1
    print("Total Employees:", count)