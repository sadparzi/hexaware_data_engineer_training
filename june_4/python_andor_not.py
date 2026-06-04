experience = 5
salary = 80000

if experience >= 3 and salary >= 50000:
    print("Eligible")
else:
    print("Not Eligible")

experience = 1
salary = 80000

if experience >= 3 or salary >= 50000:
    print("Eligible")
else:
    print("Not Eligible")

is_blocked = False

if not is_blocked:
    print("Login Allowed")