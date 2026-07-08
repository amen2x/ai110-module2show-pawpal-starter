# PawPal+ Project Reflection

## 1. System Design

**Core user actions**

A user should be able to add a pet by entering the pet's basic information, such as name, type of animal, and care needs, so the system knows who the tasks are for.

A user should be able to schedule a walk or care task for a pet by choosing what needs to happen and when it should happen.

A user should be able to see today's tasks in one place so they know what pet care responsibilities are due soon and can stay organized.

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

My initial design used four classes. `Owner` represents the user and stores their pets. `Pet` stores information about each animal and its care needs. `Task` represents a pet care responsibility, like walking, feeding, grooming, or medication. `Scheduler` manages tasks and helps show what needs to be done today.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

The initial design stayed mostly the same because the four-class structure matched the main actions of the app. I kept the design simple so each class had one clear responsibility.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

The scheduler mainly considers the time of day each task is due, along with its completion status and how often it repeats (once, daily, or weekly). Time mattered most because a daily care plan is really about the order things happen in, so sorting by time gives the owner the clearest view. Completion status and frequency were next, since they let the app hide finished work and roll recurring tasks forward.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

The scheduler uses a simple conflict detection rule: it only checks whether two tasks have the exact same time. This is easy to understand and works well for a beginner version of PawPal+, but it does not detect more complex conflicts such as overlapping task durations. I chose this tradeoff because exact-time matching keeps the logic readable while still giving the user useful warnings.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

I used an AI coding assistant across every phase: brainstorming the four-class design, generating the dataclass skeletons, implementing the sorting, recurrence, and conflict-detection algorithms, and writing the pytest tests. The most effective feature was giving the assistant a tight, phase-scoped task that named the exact method and the expected behavior (for example, "add `sort_by_time` that orders `08:00 AM`, `12:00 PM`, `06:00 PM` correctly"). Specific prompts like that produced code I could drop in with small edits, while vague prompts produced code that did too much. Using a separate chat session for each phase kept the assistant focused on one file and one goal at a time, so it did not drift into rewriting parts of the project that were already finished.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

When I connected the Streamlit UI, the assistant suggested keeping tasks as a flat list of plain dictionaries in `st.session_state`. I rejected that because it would have created two competing sources of truth and ignored the `Task` and `Pet` classes I had already built. Instead I stored a real `Owner` object in session state and had the UI create actual `Pet` and `Task` objects. I verified the change by running `streamlit run app.py` to confirm pets and tasks persisted across reruns, and by running `python -m pytest` to confirm the backend still behaved as expected.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

I tested task completion, adding tasks to a pet, sorting tasks by time, daily recurrence (creating the next occurrence), conflict detection for two tasks at the same time, and two edge cases (a new pet starting with no tasks and filtering by completion status). These behaviors are the core of the app, so testing them protects the features the user relies on and catches regressions if the code changes later.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

I am fairly confident for the current beginner-level scope, since all seven automated tests pass and cover the main algorithms. With more time I would test overlapping task durations (not just exact-time conflicts), invalid or unusual time strings, the date math for weekly recurrence, and schedules with several conflicts at once.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

I am most satisfied with the clean separation between the backend logic in `pawpal_system.py` and the Streamlit UI in `app.py`. Because the four classes each had one clear responsibility, the UI could simply call `Scheduler` methods, and the smart features (sorting, recurrence, and conflict detection) were all covered by automated tests.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

In another iteration I would upgrade conflict detection to consider task durations and overlapping time windows instead of only exact-time matches, add persistence so data survives closing the app, and let users edit or delete existing tasks from the UI.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

The biggest thing I learned was what it means to be the "lead architect" when working with powerful AI tools. The assistant could generate code quickly, but I still had to own the design decisions, keep the scope small, and verify everything by running the app and the tests. Working in separate chat sessions for each phase helped me stay organized, because each session focused on one part of the system and I could review and accept changes deliberately instead of letting the AI reshape the whole project at once.
