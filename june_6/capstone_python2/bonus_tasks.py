import csv

with open("players.csv", "r") as file:
    players = list(csv.DictReader(file))


# Task 36
# Generate top_players.csv
# Players With Runs Above 600

with open(
    "top_players.csv",
    "w",
    newline=""
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=players[0].keys()
    )

    writer.writeheader()

    for player in players:

        if int(player["runs"]) > 600:
            writer.writerow(player)


# Task 37
# Generate team_summary.csv

team_data = {}

for player in players:

    team = player["team"]
    runs = int(player["runs"])

    if team not in team_data:

        team_data[team] = {
            "total_runs": 0,
            "player_count": 0
        }

    team_data[team]["total_runs"] += runs
    team_data[team]["player_count"] += 1


with open(
    "team_summary.csv",
    "w",
    newline=""
) as file:

    fieldnames = [
        "Team",
        "Total Runs",
        "Average Runs",
        "Player Count"
    ]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()

    for team, data in team_data.items():

        average_runs = (
            data["total_runs"] /
            data["player_count"]
        )

        writer.writerow({
            "Team": team,
            "Total Runs": data["total_runs"],
            "Average Runs": average_runs,
            "Player Count": data["player_count"]
        })


print("Files Generated Successfully")