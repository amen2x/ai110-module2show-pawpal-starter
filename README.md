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

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | | e.g., by priority, duration |
| Filtering | | e.g., skip tasks if time runs out |
| Conflict handling | | e.g., overlapping time slots |
| Recurring tasks | | e.g., daily vs. weekly |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
