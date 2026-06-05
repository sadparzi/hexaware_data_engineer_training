import pandas as pd
df = pd.read_csv("employees.csv")
print(df)

print(df.head())#first 5 rows of the dataframe

print(df.tail())#first 5 rows and last 5 rows

print(df.dtypes) #data types of each column

print(df.info()) #summary of the dataframe

print(df.describe()) #statistical summary of numeric columns

print(df["name"]) #accessing a specific column

print(
    df[
        ["name", "salary"]
    ]
)
#filtering data