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

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

The scheduler uses a simple conflict detection rule: it only checks whether two tasks have the exact same time. This is easy to understand and works well for a beginner version of PawPal+, but it does not detect more complex conflicts such as overlapping task durations. I chose this tradeoff because exact-time matching keeps the logic readable while still giving the user useful warnings.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
