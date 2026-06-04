employee = (101, "Rahul", 75000)  # Packing

print(employee)

# Unpacking
emp_id, emp_name, salary = employee

print(emp_id)
print(emp_name)
print(salary)

# Multiple Values
def get_employee():
    return 101, "Rahul", 75000

result = get_employee()

print(result)

# Each Row is represented as a Tuple
record = (
    101,
    "Rahul",
    "Hyderabad",
    75000
)

print(record)