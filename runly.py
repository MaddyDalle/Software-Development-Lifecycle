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
    print()
    print("1) Add a run")
    print("2) Show all runs")
    print("3) Show total distance")
    print("4) Quit")

def add_run(runs):
    new_run = {}
    new_run["date"] = (input("Add date of your run: "))
    new_run["distance_km"] = float(input("How far did you run (km): "))
    new_run["time_min"] = float(input("How long did you run in minutes: "))
    runs.append(new_run)

def show_runs(runs):
    for run in runs: 
        print(run["date"], run["distance_km"], "km", calculate_pace(run), "min/km")

runs =[]

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_run(runs)
    elif choice == "2":
        show_runs(runs)
    elif choice == "3":
        print("Total distance:", total_distance(runs), "km")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Please choose 1, 2, 3 or 4.")