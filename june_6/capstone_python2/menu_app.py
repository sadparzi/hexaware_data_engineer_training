import csv

with open("players.csv", "r") as file:
    players = list(csv.DictReader(file))

while True:

    print("\n===== Smart Cricket Analytics System =====")
    print("1. Player Analysis")
    print("2. Team Analysis")
    print("3. Boundary Analysis")
    print("4. Export Reports")
    print("5. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:

        print("\nPlayer Analysis")

        top_scorer = players[0]

        for player in players:
            if int(player["runs"]) > int(top_scorer["runs"]):
                top_scorer = player

        total_runs = 0

        for player in players:
            total_runs += int(player["runs"])

        average_runs = total_runs / len(players)

        print("Top Scorer =", top_scorer["player_name"])
        print("Runs =", top_scorer["runs"])
        print("Average Runs =", average_runs)

    elif choice == 2:

        print("\nTeam Analysis")

        team_runs = {}

        for player in players:

            team = player["team"]
            runs = int(player["runs"])

            if team in team_runs:
                team_runs[team] += runs
            else:
                team_runs[team] = runs

        for team, runs in team_runs.items():
            print(team, "=", runs)

    elif choice == 3:

        print("\nBoundary Analysis")

        most_fours_player = players[0]
        most_sixes_player = players[0]

        total_fours = 0
        total_sixes = 0

        for player in players:

            total_fours += int(player["fours"])
            total_sixes += int(player["sixes"])

            if int(player["fours"]) > int(most_fours_player["fours"]):
                most_fours_player = player

            if int(player["sixes"]) > int(most_sixes_player["sixes"]):
                most_sixes_player = player

        print(
            "Most Fours =",
            most_fours_player["player_name"]
        )

        print(
            "Most Sixes =",
            most_sixes_player["player_name"]
        )

        print("Total Fours =", total_fours)
        print("Total Sixes =", total_sixes)

    elif choice == 4:

        total_players = len(players)

        total_runs = 0

        for player in players:
            total_runs += int(player["runs"])

        average_runs = (
            total_runs / total_players
        )

        with open(
            "cricket_report.txt",
            "w"
        ) as report:

            report.write(
                f"Total Players = {total_players}\n"
            )

            report.write(
                f"Total Runs = {total_runs}\n"
            )

            report.write(
                f"Average Runs = {average_runs}\n"
            )

        print(
            "cricket_report.txt generated successfully"
        )

    elif choice == 5:

        print("Thank You")
        break

    else:

        print("Invalid Choice")