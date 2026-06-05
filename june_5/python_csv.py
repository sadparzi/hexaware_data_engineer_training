import csv

with open(
    "employees.csv",
    "r"
) as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)