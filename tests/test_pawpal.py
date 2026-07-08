"""Quick tests for the PawPal+ logic layer."""

from datetime import date, timedelta

from pawpal_system import Owner, Pet, Task, Scheduler


def test_task_mark_complete():
    """Calling mark_complete() should change the task's status to complete."""
    task = Task("Feed Luna", "08:00 AM")
    assert task.is_complete() is False
    task.mark_complete()
    assert task.is_complete() is True


def test_add_task_increases_pet_task_count():
    """Adding a task to a pet should increase that pet's task count."""
    pet = Pet("Luna", "Cat", 3)
    assert len(pet.get_tasks()) == 0
    pet.add_task(Task("Feed Luna", "08:00 AM"))
    assert len(pet.get_tasks()) == 1


def test_sort_by_time_orders_tasks_chronologically():
    """Tasks added out of order should be returned in chronological order."""
    tasks = [
        Task("Give medication", "06:00 PM"),
        Task("Feed Luna", "08:00 AM"),
        Task("Walk Max", "12:00 PM"),
    ]
    scheduler = Scheduler()
    sorted_tasks = scheduler.sort_by_time(tasks)
    assert [task.time for task in sorted_tasks] == ["08:00 AM", "12:00 PM", "06:00 PM"]


def test_create_next_occurrence_for_daily_task():
    """A daily task should create a new task for the following day."""
    task = Task("Feed Luna", "08:00 AM", frequency="daily")
    task.mark_complete()
    scheduler = Scheduler()
    next_task = scheduler.create_next_occurrence(task)
    assert next_task is not None
    assert next_task.description == "Feed Luna"
    assert next_task.time == "08:00 AM"
    assert next_task.date == str(date.today() + timedelta(days=1))


def test_detect_conflicts_flags_same_time_tasks():
    """Two tasks at the same exact time should produce a conflict warning."""
    tasks = [Task("Feed Luna", "12:00 PM"), Task("Walk Max", "12:00 PM")]
    scheduler = Scheduler()
    warnings = scheduler.detect_conflicts(tasks)
    assert len(warnings) >= 1
    assert "12:00 PM" in warnings[0]


def test_new_pet_has_no_tasks():
    """A newly created pet should start with an empty task list."""
    pet = Pet("Mochi", "Dog", 1)
    assert pet.get_tasks() == []


def test_filter_by_completion():
    """Filtering by completion status should return only matching tasks."""
    owner = Owner("Sam", "sam@example.com")
    luna = Pet("Luna", "Cat", 3)
    owner.add_pet(luna)

    done = Task("Feed Luna", "08:00 AM")
    done.mark_complete()
    pending = Task("Walk Luna", "12:00 PM")
    luna.add_task(done)
    luna.add_task(pending)

    scheduler = Scheduler()
    all_tasks = owner.get_all_tasks()
    assert scheduler.filter_by_completion(all_tasks, True) == [done]
    assert scheduler.filter_by_completion(all_tasks, False) == [pending]
