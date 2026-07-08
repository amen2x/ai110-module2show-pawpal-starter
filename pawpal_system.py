"""PawPal+ system skeleton.

This file contains simple beginner-friendly class skeletons for the
PawPal+ pet care app. It is a skeleton only, not a finished app.
"""

from dataclasses import dataclass, field


class Owner:
    """Represents the user and stores their pets."""

    def __init__(self, name, email):
        self.name = name          # owner's name
        self.email = email        # owner's email
        self.pets = []            # list of Pet objects

    def add_pet(self, pet):
        """Add a pet to this owner."""
        pass

    def remove_pet(self, pet):
        """Remove a pet from this owner."""
        pass

    def get_pets(self):
        """Return the owner's pets."""
        return self.pets


@dataclass
class Pet:
    """Stores information about each animal and its care needs."""

    name: str
    species: str
    age: int
    care_needs: list = field(default_factory=list)  # list of care needs

    def add_care_need(self, care_need):
        """Add a care need for this pet."""
        pass

    def get_care_needs(self):
        """Return this pet's care needs."""
        return self.care_needs


@dataclass
class Task:
    """Represents a pet care responsibility (walk, feed, groom, medicate)."""

    title: str
    pet: Pet
    due_time: str
    priority: int
    completed: bool = False

    def mark_complete(self):
        """Mark this task as completed."""
        pass

    def update_due_time(self, new_due_time):
        """Change when this task is due."""
        pass

    def is_due_today(self):
        """Return True if this task is due today."""
        return False


class Scheduler:
    """Manages tasks and helps show what needs to be done today."""

    def __init__(self):
        self.tasks = []           # list of Task objects

    def add_task(self, task):
        """Add a task to the scheduler."""
        pass

    def remove_task(self, task):
        """Remove a task from the scheduler."""
        pass

    def get_today_tasks(self):
        """Return the tasks that are due today."""
        return []

    def sort_tasks_by_priority(self):
        """Return the tasks sorted by priority."""
        return self.tasks
