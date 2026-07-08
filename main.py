"""Temporary CLI demo for PawPal+.

Builds a small example owner, pets, and tasks, then prints today's schedule.
"""

from pawpal_system import Owner, Pet, Task, Scheduler


def main():
    """Create sample data and print a readable today's schedule."""
    owner = Owner("Sam", "sam@example.com")

    luna = Pet("Luna", "Cat", 3)
    max_dog = Pet("Max", "Dog", 5)

    owner.add_pet(luna)
    owner.add_pet(max_dog)

    luna.add_task(Task("Feed Luna", "08:00 AM"))
    max_dog.add_task(Task("Walk Max", "12:00 PM"))
    luna.add_task(Task("Give Luna medication", "06:00 PM"))

    scheduler = Scheduler()
    today = scheduler.get_today_schedule(owner)

    print("Today's Schedule")
    print("----------------")
    for task in today:
        print(f"{task.time} - {task.description}")


if __name__ == "__main__":
    main()
