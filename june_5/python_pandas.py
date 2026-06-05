import pandas as pd

data = {

    "employee_id": [101,102,103],

    "name": [
        "Rahul",
        "Priya",
        "Amit"
    ],

    "salary": [
        75000,
        85000,
        65000
    ]
}

df = pd.DataFrame(data)
print(df)