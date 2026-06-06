import csv

with open("players.csv", "r") as file:
    players = list(csv.DictReader(file))


# Total Players

total_players = len(players)


# Total Runs

total_runs = 0

for player in players:
    total_runs += int(player["runs"])


# Average Runs

average_runs = total_runs / total_players


# Highest Scorer

highest_scorer = players[0]

for player in players:
    if int(player["runs"]) > int(highest_scorer["runs"]):
        highest_scorer = player


# Lowest Scorer

lowest_scorer = players[0]

for player in players:
    if int(player["runs"]) < int(lowest_scorer["runs"]):
        lowest_scorer = player


# Team Wise Runs

team_runs = {}

for player in players:

    team = player["team"]
    runs = int(player["runs"])

    if team in team_runs:
        team_runs[team] += runs
    else:
        team_runs[team] = runs


# Top 5 Players

sorted_players = sorted(
    players,
    key=lambda x: int(x["runs"]),
    reverse=True
)

top_5_players = sorted_players[:5]


# Most Fours

most_fours_player = players[0]

for player in players:
    if int(player["fours"]) > int(most_fours_player["fours"]):
        most_fours_player = player


# Most Sixes

most_sixes_player = players[0]

for player in players:
    if int(player["sixes"]) > int(most_sixes_player["sixes"]):
        most_sixes_player = player


# Generate cricket_report.txt

with open("cricket_report.txt", "w") as report:

    report.write(
        f"Total Players = {total_players}\n\n"
    )

    report.write(
        f"Total Runs = {total_runs}\n\n"
    )

    report.write(
        f"Average Runs = {average_runs}\n\n"
    )

    report.write(
        f"Highest Scorer = {highest_scorer['player_name']}\n"
    )

    report.write(
        f"Runs = {highest_scorer['runs']}\n\n"
    )

    report.write(
        f"Lowest Scorer = {lowest_scorer['player_name']}\n"
    )

    report.write(
        f"Runs = {lowest_scorer['runs']}\n\n"
    )

    report.write("Team Wise Runs\n")

    for team, runs in team_runs.items():
        report.write(
            f"{team} = {runs}\n"
        )

    report.write("\nTop 5 Players\n")

    for player in top_5_players:
        report.write(
            f"{player['player_name']} = {player['runs']}\n"
        )

    report.write("\n")

    report.write(
        f"Most Fours = {most_fours_player['player_name']} ({most_fours_player['fours']})\n"
    )

    report.write(
        f"Most Sixes = {most_sixes_player['player_name']} ({most_sixes_player['sixes']})\n"
    )

print("cricket_report.txt generated successfully")