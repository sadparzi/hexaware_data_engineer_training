import csv
import numpy as np

with open("players.csv", "r") as file:
    players = list(csv.DictReader(file))


# Task 28
# Create NumPy Array Of Runs

runs = []

for player in players:
    runs.append(
        int(player["runs"])
    )

runs = np.array(runs)

print("Runs =", runs)

print("Total Runs =", np.sum(runs))

print("Average Runs =", np.mean(runs))

print("Maximum Runs =", np.max(runs))

print("Minimum Runs =", np.min(runs))

print("Standard Deviation =", np.std(runs))

print("Median =", np.median(runs))