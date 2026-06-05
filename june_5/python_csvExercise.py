import csv

with open("employees.csv", "r") as file:
    employees = list(csv.DictReader(file))


# Exercise 1
# Find Highest Salary

highest_salary = 0

for employee in employees:
    salary = int(employee["salary"])

    if salary > highest_salary:
        highest_salary = salary

print("Highest Salary =", highest_salary)


# Exercise 2
# Find Lowest Salary

lowest_salary = float("inf")

for employee in employees:
    salary = int(employee["salary"])

    if salary < lowest_salary:
        lowest_salary = salary

print("Lowest Salary =", lowest_salary)


# Exercise 3
# Find Average Salary

total_salary = 0

for employee in employees:
    total_salary += int(employee["salary"])

average_salary = total_salary / len(employees)

print("Average Salary =", average_salary)


# Exercise 4
# Find Total Salary Payout

total_salary = 0

for employee in employees:
    total_salary += int(employee["salary"])

print("Total Salary Payout =", total_salary)


# Exercise 5
# Display Hyderabad Employees

for employee in employees:
    if employee["city"] == "Hyderabad":
        print(employee)


# Exercise 6
# Display AI Engineering Employees

for employee in employees:
    if employee["department"] == "AI Engineering":
        print(employee)


# Exercise 7
# Display Employees Earning Above ₹80,000

for employee in employees:
    if int(employee["salary"]) > 80000:
        print(employee)