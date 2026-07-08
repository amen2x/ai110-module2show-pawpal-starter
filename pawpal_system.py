"""PawPal+ logic layer.

Simple, beginner-friendly classes for a small pet care app:
Owner, Pet, Task, and Scheduler.
"""

from dataclasses import dataclass, field


@dataclass
class Task:
    """One pet care activity, such as a walk or feeding."""

    description: str
    time: str
    frequency: str = "daily"
    completed: bool = False

    def mark_complete(self):
        """Mark this task as done."""
        self.completed = True

    def mark_incomplete(self):
        """Mark this task as not done."""
        self.completed = False

    def is_complete(self):
        """Return True if this task is done."""
        return self.completed


@dataclass
class Pet:
    """A pet with its details, care needs, and tasks."""

    name: str
    species: str
    age: int
    care_needs: list = field(default_factory=list)
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        """Add a task to this pet."""
        self.tasks.append(task)

    def remove_task(self, task):
        """Remove a task from this pet."""
        if task in self.tasks:
            self.tasks.remove(task)

    def get_tasks(self):
        """Return this pet's tasks."""
        return self.tasks

    def add_care_need(self, care_need):
        """Add a care need to this pet."""
        self.care_needs.append(care_need)


class Owner:
    """A pet owner who manages one or more pets."""

    def __init__(self, name, email):
        """Create an owner with a name, email, and empty pet list."""
        self.name = name
        self.email = email
        self.pets = []

    def add_pet(self, pet):
        """Add a pet to this owner."""
        self.pets.append(pet)

    def remove_pet(self, pet):
        """Remove a pet from this owner."""
        if pet in self.pets:
            self.pets.remove(pet)

    def get_pets(self):
        """Return this owner's pets."""
        return self.pets

    def get_all_tasks(self):
        """Collect and return tasks from all of this owner's pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks


class Scheduler:
    """Organizes tasks across all of an owner's pets."""

    def get_all_tasks(self, owner):
        """Return all tasks belonging to the given owner."""
        return owner.get_all_tasks()

    def sort_tasks_by_time(self, tasks):
        """Return the tasks sorted by their time of day."""
        return sorted(tasks, key=_time_to_minutes)

    def get_today_schedule(self, owner):
        """Return today's tasks for the owner, sorted by time."""
        tasks = self.get_all_tasks(owner)
        return self.sort_tasks_by_time(tasks)

    def get_pending_tasks(self, owner):
        """Return the owner's tasks that are not yet complete."""
        return [task for task in owner.get_all_tasks() if not task.is_complete()]


def _time_to_minutes(task):
    """Convert a task's time string (like '08:00 AM') into minutes for sorting."""
    time_text = task.time.strip().upper()
    period = ""
    if time_text.endswith("AM") or time_text.endswith("PM"):
        period = time_text[-2:]
        time_text = time_text[:-2].strip()

    hours, minutes = time_text.split(":")
    hours = int(hours)
    minutes = int(minutes)

    if period == "PM" and hours != 12:
        hours += 12
    if period == "AM" and hours == 12:
        hours = 0

    return hours * 60 + minutes
