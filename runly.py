def calculate_pace(run):
    return run["time_min"] / run["distance_km"]

def total_distance(runs):
    total = 0
    for run in runs:
        total = total + run["distance_km"]
    return total

def show_menu():
    print()
    print("=== RUNLY ===")
    print("1) Add a run")
    print("2) Show all runs")
    print("3) Show total distance")
    print("4) Quit")

show_menu()

runs =[]

new_run = {}

new_run["date"] = (input("Add date of your run: "))
new_run["distance_km"] = float(input("How far did you run (km): "))
new_run["time_min"] = int(input("How fast did you run in minutes: "))

runs.append(new_run)

for run in runs: 
    print(run["date"], run["distance_km"], "km", calculate_pace(run), "min/km")

print("Total distance:", total_distance(runs), "km")