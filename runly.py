def calculate_pace(run):
    return run["time_min"] / run["distance_km"]

def total_distance(runs):
    total = 0
    for run in runs:
        total = total + run["distance_km"]
    return total

def longest_run(runs):
    if len(runs) == 0:
        return None
    longest = runs[0]
    for run in runs:
        if run["distance_km"] > longest["distance_km"]:
            longest = run
    return longest

def average_pace(runs): 
    if len(runs) == 0:
        return None
    total_time = 0 
    for run in runs: 
        total_time = total_time + run["time_min"]
    return total_time / total_distance(runs)

def add_run(runs):
    new_run = {}
    new_run["date"] = (input("Add date of your run: "))
    new_run["distance_km"] = ask_number("How far did you run (km): ")
    new_run["time_min"] = ask_number("How long did you run in minutes: ")
    runs.append(new_run)

def show_runs(runs):
    if len(runs) == 0:
        print ("No runs yet.")
    for run in runs: 
        print(run["date"], run["distance_km"], "km", calculate_pace(run), "min/km")


def show_menu():
    print()
    print("=== RUNLY ===")
    print()
    print("1) Add a run")
    print("2) Show all runs")
    print("3) Show total distance")
    print("4) Show longest run")
    print("5) Show average page")
    print("6) Quit")

def ask_number(question):
    while True:
        answer = input(question)
        try:
            number = float(answer)
        except ValueError:
            print("Please enter a number!")
            continue
        if number <= 0:
            print("Please enter a number greater than 0!")
            continue
        return number

runs =[]

while True:
    show_menu()
    choice = input("Choose an option (1-6): ")

    if choice == "1":
        add_run(runs)
    elif choice == "2":
        show_runs(runs)
    elif choice == "3":
        print("Total distance: ", total_distance(runs), "km")
    elif choice == "4":
        longest = longest_run(runs)
        if longest is None:
            print("No runs yet.")
        else:
            print("Longest run:", longest["date"], "-", longest["distance_km"], "km")
    elif choice == "5":
        average = average_pace(runs)
        if average is None:
            print("No runs yet.")
        else:
            print("Average pace:", average, "min/km")
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Please choose 1, 2, 3, 4, 5 or 6.")