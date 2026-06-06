import csv


# Task 25
# Handle Missing CSV File

try:

    with open("players.csv", "r") as file:
        players = list(csv.DictReader(file))

    print("File Loaded Successfully")

except FileNotFoundError:

    print("players.csv file not found")


# Task 26
# Handle Invalid Run Values

try:

    with open("players.csv", "r") as file:
        players = list(csv.DictReader(file))

    total_runs = 0

    for player in players:

        runs = int(player["runs"])

        total_runs += runs

    print("Total Runs =", total_runs)

except ValueError:

    print("Invalid Run Value Found")


# Task 27
# Handle Invalid Match Counts

try:

    with open("players.csv", "r") as file:
        players = list(csv.DictReader(file))

    total_matches = 0

    for player in players:

        matches = int(player["matches"])

        total_matches += matches

    print("Total Matches =", total_matches)

except ValueError:

    print("Invalid Match Count Found")