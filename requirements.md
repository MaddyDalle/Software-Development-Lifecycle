# RUNLY – Requirements

## Problem

Many people want to start running or improve their results, but don't know how to structure their training and increase the load gradually.

## Goal

A simple command-line version of RUNLY, a personalised running training app, built step by step.

## Version 1 - Run log

- As a runner, I want to add a run (date, distance in km, time in minutes).
- As a runner, I want to see a list of all my runs.
- As a runner, I want to see my pace for each run (min/km).
- As a runner, I want to see my total distance.

## Later versions

- v2: Runner profile with a goal (5 km, 10 km, half marathon) and level
- v3: Simple weekly training plan based on goal and available days
- v4: Free users see the next 4 workouts, Premium users see the full plan
- v5: Wellbeing an womans cycle tracking alongside runs

## Out of scope

AI-generated plans, sports watch integration, mobile app, payments. (I am not that skilled... yet.)

## Technical requirements

- Tests: automated tests for calculate_pace and total_distance.
- Automation: tests run automatically on GitHub on every push.
- Database: runs are saved in a SQLite database so they are kept after the program closes.
- Migrations: every change to the database structure is a numbered migration file
  (e.g. 001_create_runs_table.sql).