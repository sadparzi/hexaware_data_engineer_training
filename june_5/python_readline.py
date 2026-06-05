file = open(
    "employees.txt",
    "r"
)

print(file.readline())

file.close()
#read multiple lines
file = open(
    "employees.txt",
    "r"
)

lines = file.readlines()

print(lines)

file.close()

#automatically close the file using with statement
with open(
    "employees.txt",
    "r"
) as file:

    data = file.read()
    print(data)