"""Quick tests for the PawPal+ logic layer."""

from pawpal_system import Pet, Task


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
