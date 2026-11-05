def calculate_pace(run):
    return run["time_min"] / run["distance_km"]

def total_distance(runs):
    total = 0
    for run in runs:
        total = total + run["distance_km"]
    return total

runs =[]

new_run = {}

new_run["date"] = (input("Add date of your run: "))
new_run["distance_km"] = float(input("How far did you run (in km): "))
new_run["time_min"] = int(input("How fast did you run in minutes: "))

runs.append(new_run)

for run in runs: 
    print(run["date"], run["distance_km"], "km", calculate_pace(run), "min/km")

print("Total distance:", total_distance(runs), "km")