def calculate_pace(run):
    return run["time_min"] / run["distance_km"]

run = {"date": "2026-10-31", "distance_km": 5.0, "time_min": 30.0}

print(run)
print("Average pace: ", calculate_pace(run), "min/km")