import streamlit as st

from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This app connects the Streamlit UI to the backend classes in `pawpal_system.py`.
Add pets, schedule their care tasks, and see today's schedule.
"""
)

with st.expander("Scenario", expanded=False):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.
"""
    )

# Create the Owner once and keep it in session state so data survives reruns.
if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="Demo Owner", email="demo@example.com")

owner = st.session_state.owner

st.divider()

# --- Add Pet -----------------------------------------------------------------
st.subheader("Add a Pet")

with st.form("add_pet_form"):
    pet_name = st.text_input("Pet name", value="Mochi")
    species = st.selectbox("Species", ["dog", "cat", "other"])
    age = st.number_input("Age (years)", min_value=0, max_value=50, value=1)
    add_pet_clicked = st.form_submit_button("Add pet")

if add_pet_clicked:
    new_pet = Pet(name=pet_name, species=species, age=int(age))
    owner.add_pet(new_pet)
    st.success(f"Added {new_pet.name} ({new_pet.species}).")

# Show the current pets (stored inside the Owner object).
pets = owner.get_pets()
if pets:
    st.write("Your pets:")
    for pet in pets:
        st.write(f"- {pet.name} ({pet.species}, {pet.age} yrs)")
else:
    st.info("No pets yet. Add one above.")

st.divider()

# --- Schedule Task -----------------------------------------------------------
st.subheader("Schedule a Task")

if pets:
    with st.form("add_task_form"):
        pet_names = [pet.name for pet in pets]
        chosen_pet_name = st.selectbox("Pet", pet_names)
        description = st.text_input("Task description", value="Morning walk")
        time = st.text_input("Time (for example 08:00 AM)", value="08:00 AM")
        add_task_clicked = st.form_submit_button("Add task")

    if add_task_clicked:
        chosen_pet = next(pet for pet in pets if pet.name == chosen_pet_name)
        new_task = Task(description=description, time=time)
        chosen_pet.add_task(new_task)
        st.success(f"Added '{new_task.description}' for {chosen_pet.name}.")
else:
    st.info("Add a pet first to schedule tasks.")

st.divider()

# --- Today's Schedule --------------------------------------------------------
st.subheader("Today's Schedule")

scheduler = Scheduler()
today = scheduler.get_today_schedule(owner)

if today:
    for task in today:
        st.write(f"{task.time} - {task.description}")
else:
    st.info("No tasks scheduled yet.")
