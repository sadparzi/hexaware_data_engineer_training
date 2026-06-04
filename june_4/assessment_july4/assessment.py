salaries = [45000, 55000, 65000, 75000, 85000]

# Exercise 1
for salary in salaries:
    print(salary)

# Exercise 2
print("Maximum Salary:", max(salaries))
print("Minimum Salary:", min(salaries))

# Exercise 3
print("Total Salary Payout:", sum(salaries))

# Exercise 4
print("Average Salary:", sum(salaries) / len(salaries))

# Exercise 5
salaries.append(95000)
salaries.append(105000)
print(salaries)

# Exercise 6
salaries.remove(55000)
print(salaries)

# Exercise 7
salaries.sort()
print(salaries)

# Exercise 8
salaries.sort(reverse=True)
print(salaries)

# Exercise 9
print("Second Highest Salary:", salaries[1])

# Exercise 10
for salary in salaries:
    if salary > 70000:
        print(salary)

employee = (
    101,
    "Rahul Sharma",
    "Data Engineering",
    75000
)

# Exercise 11
print(employee)

# Exercise 12
print(employee[1])

# Exercise 13
print(employee[2])

# Exercise 14
emp_id, emp_name, department, salary = employee

print(emp_id)
print(emp_name)
print(department)
print(salary)

# Exercise 15
print("Length:", len(employee))
print("First Element:", employee[0])
print("Last Element:", employee[-1])

batch_a = {
    "Rahul",
    "Priya",
    "Amit",
    "Sneha",
    "Farhan"
}

batch_b = {
    "Priya",
    "Sneha",
    "Neha",
    "Arjun",
    "Farhan"
}

# Exercise 16
print(batch_a.intersection(batch_b))

# Exercise 17
print(batch_a.difference(batch_b))

# Exercise 18
print(batch_b.difference(batch_a))

# Exercise 19
print(batch_a.union(batch_b))

# Exercise 20
print(batch_a.symmetric_difference(batch_b))

employee_info = {
    "employee_id": 101,
    "name": "Rahul Sharma",
    "department": "Data Engineering",
    "salary": 75000,
    "city": "Hyderabad"
}

# Exercise 21
print(employee_info["name"])

# Exercise 22
print(employee_info["department"])
print(employee_info["city"])

# Exercise 23
employee_info["experience"] = 5
print(employee_info)

# Exercise 24
employee_info["salary"] = 85000
print(employee_info)

# Exercise 25
employee_info.pop("city")
print(employee_info)

# Exercise 26
print(employee_info.keys())

# Exercise 27
print(employee_info.values())

# Exercise 28
print(employee_info.items())

employees = [
    {
        "id": 101,
        "name": "Rahul",
        "department": "IT",
        "salary": 50000
    },
    {
        "id": 102,
        "name": "Priya",
        "department": "HR",
        "salary": 70000
    },
    {
        "id": 103,
        "name": "Amit",
        "department": "IT",
        "salary": 60000
    },
    {
        "id": 104,
        "name": "Sneha",
        "department": "Finance",
        "salary": 80000
    },
    {
        "id": 105,
        "name": "Farhan",
        "department": "IT",
        "salary": 90000
    }
]

# Exercise 29
for employee in employees:
    print(employee["name"])

# Exercise 30
for employee in employees:
    if employee["department"] == "IT":
        print(employee)

# Exercise 31
print(max(employees, key=lambda x: x["salary"]))

# Exercise 32
print(min(employees, key=lambda x: x["salary"]))

# Exercise 33
total = sum(employee["salary"] for employee in employees)
print(total / len(employees))

# Exercise 34
print(sum(employee["salary"] for employee in employees))

# Exercise 35
for employee in employees:
    if employee["salary"] > 70000:
        print(employee)

# Exercise 36
count = 0
for employee in employees:
    if employee["department"] == "IT":
        count += 1
print(count)

# Exercise 37
sorted_employees = sorted(
    employees,
    key=lambda x: x["salary"],
    reverse=True
)

for employee in sorted_employees:
    print(employee["name"])

# Exercise 38
sorted_employees = sorted(
    employees,
    key=lambda x: x["salary"],
    reverse=True
)

print(sorted_employees[1])

# Exercise 39
departments = set()

for employee in employees:
    departments.add(employee["department"])

print(departments)
