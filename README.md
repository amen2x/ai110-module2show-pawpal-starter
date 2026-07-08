# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Features

- **Add pets** — store each pet's name, species, age, and care needs.
- **Schedule care tasks** — add tasks (feeding, walks, medication, grooming) with a time and frequency.
- **Sorting by time** — the schedule is ordered chronologically, handling `AM`/`PM` times (`Scheduler.sort_by_time()`).
- **Conflict warnings** — flags when two tasks are set for the exact same time (`Scheduler.detect_conflicts()`).
- **Daily/weekly recurrence** — creates the next occurrence of a repeating task after it is completed (`Scheduler.create_next_occurrence()`).
- **Filtering** — view tasks for a single pet or by completion status (`Scheduler.filter_by_pet()`, `Scheduler.filter_by_completion()`).

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## Sample Output

```text
Today's Schedule
----------------
08:00 AM - Feed Luna
12:00 PM - Walk Max
06:00 PM - Give Luna medication
```

## Testing PawPal+

Run the automated test suite with:

```bash
python -m pytest
```

The tests cover:

- task completion
- adding tasks to pets
- sorting tasks by time
- recurring daily tasks
- conflict detection
- basic edge cases (a pet with no tasks, filtering by completion status)

Successful run:

```text
============================= test session starts =============================
platform win32 -- Python 3.13.14, pytest-9.0.3, pluggy-1.6.0
collected 7 items

tests\test_pawpal.py .......                                             [100%]

============================== 7 passed in 0.05s ==============================
```

### Confidence Level

★★★★☆ 4/5

The system is reliable for the current beginner-level features because the main class behavior, sorting, recurrence, and conflict detection are covered by automated tests. More complex real-world scheduling cases would need additional tests later.

## Smarter Scheduling

The `Scheduler` class provides simple algorithmic helpers:

- **Sorting** — `Scheduler.sort_by_time()` returns tasks ordered by time of day (handles `AM`/`PM`).
- **Filtering** — `Scheduler.filter_by_pet()` returns the tasks for one pet, and `Scheduler.filter_by_completion()` returns tasks that are complete or pending.
- **Conflict detection** — `Scheduler.detect_conflicts()` returns warning messages when two tasks share the exact same time.
- **Recurring tasks** — `Scheduler.create_next_occurrence()` creates the next `daily` (+1 day) or `weekly` (+7 days) task, and returns `None` for `once`.

## Demo Walkthrough

The Streamlit app (`streamlit run app.py`) has three main areas:

1. **Add a Pet** — enter a name, species, and age, then click **Add pet**. A success message confirms it, and the pet appears in "Your pets". Pets persist across reruns because they are stored on the `Owner` in `st.session_state`.
2. **Schedule a Task** — pick one of your pets, type a task description and a time (e.g. `08:00 AM`), then click **Add task**. The task is attached to that pet.
3. **Today's Schedule** — shows all tasks across pets in a table, automatically **sorted by time**, with a **Status** column (Done/Pending). If two tasks share the exact same time, a yellow **conflict warning** appears above the table so the owner notices it immediately.

**Example workflow:** add a pet (Luna) → schedule a task ("Feed Luna" at `08:00 AM`) → add another pet (Max) → schedule "Walk Max" at `12:00 PM` → open Today's Schedule to see the ordered plan. Adding a second task at `12:00 PM` triggers a conflict warning.

**Key Scheduler behaviors shown:** chronological sorting (`sort_by_time`), conflict warnings (`detect_conflicts`), completion status, and (in the CLI demo) daily recurrence (`create_next_occurrence`).

### CLI Demo Output

Running `python main.py` demonstrates the same logic in the terminal:

```text
Original Schedule (unsorted)
----------------------------
06:00 PM - Give Luna medication
08:00 AM - Feed Luna
12:00 PM - Walk Max

Sorted Schedule
---------------
08:00 AM - Feed Luna
12:00 PM - Walk Max
06:00 PM - Give Luna medication

Tasks for Luna
--------------
06:00 PM - Give Luna medication
08:00 AM - Feed Luna

Completed Tasks
---------------
08:00 AM - Feed Luna

Pending Tasks
-------------
06:00 PM - Give Luna medication
12:00 PM - Walk Max

Recurring Task
--------------
Completed: Feed Luna (daily)
Next occurrence: Feed Luna at 08:00 AM on 2026-07-08

Conflict Warnings
-----------------
Conflict: Groom Luna and Walk Max are both scheduled at 12:00 PM.
```
