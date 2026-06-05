# Multiple Exceptions

try:
    age = int(input("Enter Age: "))
    print(100 / age)

except ValueError:
    print("Invalid Number")

except ZeroDivisionError:
    print("Age cannot be zero")


# Exception Object

try:
    num = int("abc")

except Exception as e:
    print(e)


# Else Block

try:
    num = 10
    print(num)

except:
    print("Error")

else:
    print("Success")