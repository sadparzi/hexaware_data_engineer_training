# Exercise 1
with open("employees.txt", "r") as file:
    print(file.read())

# Exercise 2
with open("employees.txt", "r") as file:
    for line in file:
        print(line.strip())

# Exercise 3
count = 0

with open("employees.txt", "r") as file:
    for line in file:
        count += 1

print("Total Employees =", count)

# Exercise 4
with open("employees.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        print(data[1])

# Exercise 5
with open("employees.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        if data[4] == "Hyderabad":
            print(data)

# Exercise 6
with open("employees.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        if data[4] == "Bangalore":
            print(data)

# Exercise 7
with open("employees.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        if int(data[3]) > 80000:
            print(data)

# Exercise 8
highest_salary = 0

with open("employees.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        salary = int(data[3])

        if salary > highest_salary:
            highest_salary = salary

print("Highest Salary =", highest_salary)

# Exercise 9
lowest_salary = float('inf')

with open("employees.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        salary = int(data[3])

        if salary < lowest_salary:
            lowest_salary = salary

print("Lowest Salary =", lowest_salary)

# Exercise 10
total_salary = 0
count = 0

with open("employees.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        total_salary += int(data[3])
        count += 1

print("Average Salary =", total_salary / count)


# Exercise 11
total_salary = 0

with open("employees.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        total_salary += int(data[3])

print("Total Salary =", total_salary)


# Exercise 12
count = 0

with open("employees.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")

        if data[2] == "AI Engineering":
            count += 1

print("AI Engineering =", count)


# Exercise 13
count = 0

with open("employees.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")

        if data[2] == "Data Engineering":
            count += 1

print("Data Engineering =", count)


# Exercise 14
with open("employees.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")

        if data[2] == "AI Engineering":
            print(data)


# Exercise 15
with open("employees.txt", "r") as file, \
     open("high_salary_employees.txt", "w") as output:

    for line in file:
        data = line.strip().split(",")

        if int(data[3]) > 80000:
            output.write(line)


# Exercise 16
with open("employees.txt", "r") as file, \
     open("hyderabad_employees.txt", "w") as output:

    for line in file:
        data = line.strip().split(",")

        if data[4] == "Hyderabad":
            output.write(line)


# Exercise 17
cities = set()

with open("employees.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        cities.add(data[4])

for city in cities:
    print(city)


# Exercise 18
departments = {}

with open("employees.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        dept = data[2]

        if dept in departments:
            departments[dept] += 1
        else:
            departments[dept] = 1

for dept, count in departments.items():
    print(dept, "=", count)


# Exercise 19
highest_salary = 0
employee_name = ""

with open("employees.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        salary = int(data[3])

        if salary > highest_salary:
            highest_salary = salary
            employee_name = data[1]

print(employee_name)
print(highest_salary)


# Exercise 20
total_salary = 0
count = 0
highest_salary = 0
lowest_salary = float("inf")

with open("employees.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        salary = int(data[3])

        total_salary += salary
        count += 1

        if salary > highest_salary:
            highest_salary = salary

        if salary < lowest_salary:
            lowest_salary = salary

average_salary = total_salary / count

with open("employee_report.txt", "w") as report:
    report.write(f"Total Employees = {count}\n")
    report.write(f"Highest Salary = {highest_salary}\n")
    report.write(f"Lowest Salary = {lowest_salary}\n")
    report.write(f"Average Salary = {average_salary}\n")
    report.write(f"Total Salary = {total_salary}\n")