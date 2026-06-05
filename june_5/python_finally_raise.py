try:
    print(10 / 0)

except:
    print("Error")

finally:
    print("Connection Closed")

salary = -1000

if salary < 0:
    raise ValueError(
        "Salary cannot be negative"
    )