import re

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
    new_run["date"] = ask_date("Add date of your run (YYYY-MM-DD): ")
    new_run["distance_km"] = ask_number("How far did you run (km): ")
    new_run["time_min"] = ask_number("How long did you run in minutes: ")
    runs.append(new_run)

def ask_date(question): 
    while True: 
        answer = input(question)
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", answer):
            return answer
        print("Please enter the date as YYYY-MM-DD, for example 2026-11-05")

def format_pace(pace): 
    minutes = int(pace)
    seconds = round((pace - minutes) * 60)
    return f"{minutes}:{seconds:02d}"

def show_runs(runs):
    if len(runs) == 0:
        print ("No runs yet.")
    for run in runs: 
        print(run["date"], run["distance_km"], "km", format_pace(calculate_pace(run)), "min/km")


def show_menu():
    print()
    print("=== RUNLY ===")
    print()
    print("1) Add a run")
    print("2) Show all runs")
    print("3) Show total distance")
    print("4) Show longest run")
    print("5) Show average page")
    print("6) Show profile")
    print("7) Quit")

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
    
def create_profile():
    name = input("What is your name? ")
    while True:
        print()
        print("Choose your goal:")
        print("1) 5 km")
        print("2) 10 km")
        print("3) Half marathon")
        choice = input("Your goal (1-3): ")
        if choice == "1":
            goal_km = 5.0
            break
        elif choice == "2":
            goal_km = 10.0
            break
        elif choice == "3":
            goal_km = 21.1
            break
        else:
            print("Please choose 1, 2 or 3.")
    return {"name": name, "goal_km": goal_km}

def show_profile(profile, runs):
    print("Runner:", profile["name"])
    print("Goal:", profile["goal_km"], "km")
    longest = longest_run(runs)
    if longest is None:
        print("No runs yet - time to start training!")
    elif longest["distance_km"] >= profile["goal_km"]:
        print("Goal reached! Longest run:", longest["distance_km"], "km")
    else:
        remaining = profile["goal_km"] - longest["distance_km"]
        print("Longest run:", longest["distance_km"], "km -", round(remaining, 1), "km to go")

runs =[]

profile = create_profile()
print(f"Welcome, {profile['name']}! Your goal: {profile['goal_km']} km")

while True:
    show_menu()
    choice = input("Choose an option (1-7): ")

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
            print("Average pace:", format_pace(average), "min/km")
    elif choice == "6":
        show_profile(profile, runs)
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Please choose a number from 1 to 7.")