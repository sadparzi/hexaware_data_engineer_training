import json

with open("employees.json", "r") as file:
    employees = json.load(file)

print(employees)

# Print All Employees
for employee in employees:
    print(employee)

# Print Employee Names
for employee in employees:
    print(employee["name"])

# Find Number of Employees
print(len(employees))

# Highest Salary
highest_salary = 0

for employee in employees:
    if employee["salary"] > highest_salary:
        highest_salary = employee["salary"]

print(highest_salary)