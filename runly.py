def calculate_pace(run):
    return run["time_min"] / run["distance_km"]

def total_distance(runs):
    total = 0
    for run in runs:
        total = total + run["distance_km"]
    return total

runs =[
    {"date": "2026-10-31", "distance_km": 5.0, "time_min": 30.0},
    {"date": "2026-10-29", "distance_km": 3.0, "time_min": 19.5},
    {"date": "2026-10-31", "distance_km": 10.0, "time_min": 55.0}]

for run in runs: 
    print(run["date"], run["distance_km"], "km", calculate_pace(run), "min/km")

print("Total distance:", total_distance(runs), "km")