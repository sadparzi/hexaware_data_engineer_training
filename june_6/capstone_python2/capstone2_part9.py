import pandas as pd


# Task 29
# Read CSV Using Pandas

df = pd.read_csv("players.csv")

print(df)


# Task 30
# Display Top 5 Run Scorers

top_5_players = df.sort_values(
    by="runs",
    ascending=False
).head(5)

print(top_5_players)


# Task 31
# Display Players Sorted By Runs Descending

sorted_players = df.sort_values(
    by="runs",
    ascending=False
)

print(sorted_players)


# Task 32
# Group By Team And Calculate Total Runs

team_runs = df.groupby(
    "team"
)["runs"].sum()

print(team_runs)


# Task 33
# Group By Team And Calculate Average Runs

team_average_runs = df.groupby(
    "team"
)["runs"].mean()

print(team_average_runs)


# Task 34
# Display Players With Runs > 600

players_above_600 = df[
    df["runs"] > 600
]

print(players_above_600)


# Task 35
# Find Top Team

team_runs = df.groupby(
    "team"
)["runs"].sum()

top_team = team_runs.idxmax()

print("Top Team =", top_team)

print(
    "Runs =",
    team_runs[top_team]
)