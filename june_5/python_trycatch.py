try:
    a = 10
    b = 0
    result = a / b
    print(result)
except:
    print("Error: Division by zero is not allowed.")

print("Program Completed")
#specific exceptions 
try:
    a = 10
    b = 0
    result = a / b
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

print("Program Completed")

try:
    age = int(input("Enter your age: "))
    print(age)
except ValueError:
    print("Error: Invalid input. Please enter numeric value for age.")