import json

with open("employees.json", "r") as file:
    employees = json.load(file)


# Exercise 1
# Find Employee With Highest Salary

highest_salary_employee = employees[0]

for employee in employees:
    if employee["salary"] > highest_salary_employee["salary"]:
        highest_salary_employee = employee

print(highest_salary_employee)


# Exercise 2
# Find Average Salary

total_salary = 0

for employee in employees:
    total_salary += employee["salary"]

print(total_salary / len(employees))


# Exercise 3
# Display Data Engineering Employees

for employee in employees:
    if employee["department"] == "Data Engineering":
        print(employee)


# Exercise 4
# Display Employees Earning More Than 80000

for employee in employees:
    if employee["salary"] > 80000:
        print(employee)


# Exercise 5
# Update Salary of Employee 101

for employee in employees:
    if employee["employee_id"] == 101:
        employee["salary"] = 85000

print(employees)

with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)


# Exercise 6
# Add New Employee

new_employee = {
    "employee_id": 106,
    "name": "Neha Singh",
    "department": "AI Engineering",
    "salary": 72000,
    "city": "Hyderabad"
}

employees.append(new_employee)

print(employees)

with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)


# Exercise 7
# Delete Employee 106

for employee in employees:
    if employee["employee_id"] == 106:
        employees.remove(employee)
        break

print(employees)

with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)