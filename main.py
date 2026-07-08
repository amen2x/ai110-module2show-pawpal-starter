"""Temporary CLI demo for PawPal+.

Shows the smarter scheduling features: sorting, filtering,
recurring tasks, and conflict detection.
"""

from pawpal_system import Owner, Pet, Task, Scheduler


def print_schedule(title, tasks):
    """Print a titled, readable list of tasks."""
    print(title)
    print("-" * len(title))
    for task in tasks:
        print(f"{task.time} - {task.description}")
    print()


def main():
    """Create sample data and demonstrate the scheduling algorithms."""
    owner = Owner("Sam", "sam@example.com")

    luna = Pet("Luna", "Cat", 3)
    max_dog = Pet("Max", "Dog", 5)
    owner.add_pet(luna)
    owner.add_pet(max_dog)

    # Add tasks out of time order.
    luna.add_task(Task("Give Luna medication", "06:00 PM"))
    max_dog.add_task(Task("Walk Max", "12:00 PM"))
    feed_luna = Task("Feed Luna", "08:00 AM", frequency="daily")
    luna.add_task(feed_luna)

    scheduler = Scheduler()
    all_tasks = scheduler.get_all_tasks(owner)

    # 1. Original (unsorted) order.
    print_schedule("Original Schedule (unsorted)", all_tasks)

    # 2. Sorted by time.
    print_schedule("Sorted Schedule", scheduler.sort_by_time(all_tasks))

    # 3. Filter by pet.
    print_schedule("Tasks for Luna", scheduler.filter_by_pet(owner, "Luna"))

    # 4. Filter by completion status.
    feed_luna.mark_complete()
    print_schedule(
        "Completed Tasks", scheduler.filter_by_completion(all_tasks, True)
    )
    print_schedule(
        "Pending Tasks", scheduler.filter_by_completion(all_tasks, False)
    )

    # 5. Recurring task: create the next occurrence after completion.
    next_feed = scheduler.create_next_occurrence(feed_luna)
    print("Recurring Task")
    print("--------------")
    print(f"Completed: {feed_luna.description} ({feed_luna.frequency})")
    print(
        f"Next occurrence: {next_feed.description} at {next_feed.time} "
        f"on {next_feed.date}"
    )
    print()

    # 6. Conflict detection: add a task at the same time as another.
    luna.add_task(Task("Groom Luna", "12:00 PM"))
    conflicts = scheduler.detect_conflicts(scheduler.get_all_tasks(owner))
    print("Conflict Warnings")
    print("-----------------")
    if conflicts:
        for warning in conflicts:
            print(warning)
    else:
        print("No conflicts found.")


if __name__ == "__main__":
    main()
