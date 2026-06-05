with open(
    "employees1.txt",
    "w"
) as file:

    file.write(
        "Rahul\n"
    )

    file.write(
        "Priya\n"
    )

# append
with open(
    "employees1.txt",
    "a"
) as file:

    file.write(
        "Amit\n"
    )