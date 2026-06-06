import csv

with open("players.csv", "r") as file:
    players = list(csv.DictReader(file))


# Part 1 – File Handling

# Task 1
# Read players.csv

print(players)


# Task 2
# Display all records

for player in players:
    print(player)


# Task 3
# Count total players

print("Total Players =", len(players))


# Part 2 – Player Analytics

# Task 4
# Find Highest Run Scorer

top_scorer = players[0]

for player in players:
    if int(player["runs"]) > int(top_scorer["runs"]):
        top_scorer = player

print(top_scorer)


# Task 5
# Find Lowest Run Scorer

lowest_scorer = players[0]

for player in players:
    if int(player["runs"]) < int(lowest_scorer["runs"]):
        lowest_scorer = player

print(lowest_scorer)


# Task 6
# Calculate Average Runs

total_runs = 0

for player in players:
    total_runs += int(player["runs"])

average_runs = total_runs / len(players)

print("Average Runs =", average_runs)


# Task 7
# Display Players Scoring More Than 600 Runs

for player in players:
    if int(player["runs"]) > 600:
        print(player)


# Task 8
# Display Players Scoring Less Than 500 Runs

for player in players:
    if int(player["runs"]) < 500:
        print(player)


# Part 3 – Team Analytics

# Task 9
# Count Players By Team

team_count = {}

for player in players:
    team = player["team"]

    if team in team_count:
        team_count[team] += 1
    else:
        team_count[team] = 1

print(team_count)


# Task 10
# Calculate Total Runs By Team

team_runs = {}

for player in players:
    team = player["team"]
    runs = int(player["runs"])

    if team in team_runs:
        team_runs[team] += runs
    else:
        team_runs[team] = runs

print(team_runs)


# Task 11
# Find Team With Highest Runs

team_runs = {}

for player in players:
    team = player["team"]
    runs = int(player["runs"])

    if team in team_runs:
        team_runs[team] += runs
    else:
        team_runs[team] = runs

top_team = max(
    team_runs,
    key=team_runs.get
)

print("Top Team =", top_team)
print("Runs =", team_runs[top_team])


# Task 12
# Find Team With Lowest Runs

team_runs = {}

for player in players:
    team = player["team"]
    runs = int(player["runs"])

    if team in team_runs:
        team_runs[team] += runs
    else:
        team_runs[team] = runs

lowest_team = min(
    team_runs,
    key=team_runs.get
)

print("Lowest Team =", lowest_team)
print("Runs =", team_runs[lowest_team])