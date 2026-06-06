import csv

with open("players.csv", "r") as file:
    players = list(csv.DictReader(file))


# Part 4 – Boundary Analysis

# Task 13
# Find Player With Most Fours

most_fours_player = players[0]

for player in players:
    if int(player["fours"]) > int(most_fours_player["fours"]):
        most_fours_player = player

print(most_fours_player)


# Task 14
# Find Player With Most Sixes

most_sixes_player = players[0]

for player in players:
    if int(player["sixes"]) > int(most_sixes_player["sixes"]):
        most_sixes_player = player

print(most_sixes_player)


# Task 15
# Calculate Total Fours Hit In Tournament

total_fours = 0

for player in players:
    total_fours += int(player["fours"])

print("Total Fours =", total_fours)


# Task 16
# Calculate Total Sixes Hit In Tournament

total_sixes = 0

for player in players:
    total_sixes += int(player["sixes"])

print("Total Sixes =", total_sixes)


# Part 5 – Lists, Sets and Dictionaries

# Task 17
# Store All Player Names In A List And Sort Alphabetically

player_names = []

for player in players:
    player_names.append(player["player_name"])

player_names.sort()

print(player_names)


# Task 18
# Store All Teams In A Set And Display Unique Teams

teams = set()

for player in players:
    teams.add(player["team"])

for team in teams:
    print(team)


# Task 19
# Create Dictionary {team : total_runs}

team_runs = {}

for player in players:
    team = player["team"]
    runs = int(player["runs"])

    if team in team_runs:
        team_runs[team] += runs
    else:
        team_runs[team] = runs

print(team_runs)


# Task 20
# Create Dictionary {player_name : runs}

player_runs = {}

for player in players:
    player_runs[player["player_name"]] = int(player["runs"])

print(player_runs)


# Part 6 – Functions

# Task 21
# find_top_scorer()

def find_top_scorer():

    top_scorer = players[0]

    for player in players:
        if int(player["runs"]) > int(top_scorer["runs"]):
            top_scorer = player

    return top_scorer["player_name"]


print("Top Scorer =", find_top_scorer())


# Task 22
# calculate_average_runs()

def calculate_average_runs():

    total_runs = 0

    for player in players:
        total_runs += int(player["runs"])

    return total_runs / len(players)


print("Average Runs =", calculate_average_runs())


# Task 23
# find_best_team()

def find_best_team():

    team_runs = {}

    for player in players:

        team = player["team"]
        runs = int(player["runs"])

        if team in team_runs:
            team_runs[team] += runs
        else:
            team_runs[team] = runs

    return max(team_runs, key=team_runs.get)


print("Best Team =", find_best_team())


# Task 24
# find_total_boundaries()

def find_total_boundaries():

    total_boundaries = 0

    for player in players:
        total_boundaries += (
            int(player["fours"]) +
            int(player["sixes"])
        )

    return total_boundaries


print("Total Boundaries =", find_total_boundaries())