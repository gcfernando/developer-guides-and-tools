# Course writing rules

Write for a reader who has never studied machine learning or written code.

- Use simple English and short sentences. Keep a respectful tone for adults.
- Explain a new word before using it. Keep the correct technical name beside the simple explanation.
- Teach one new idea at a time. Show a small example before code or a formula.
- Explain where to click, which file to open, what to change, how to save, and what to run.
- Give each lesson a goal, prior skills, a prediction question, numbered steps, a result check, a small change, a recovery step, and an explained answer.
- Explain why a step matters. A command that works is not proof that the learner understands it.
- Keep measured answers separate from invented requests. Do not score an edited request against an old measured answer.
- Use the main learning path for required skills. Mark extra topics as optional and name their prior skills.
- Keep Python names, file names, units and numerical results accurate. Simple language must not change the meaning.
- The editable lesson files are in `lessons/`. Build the ZIPs and browser pages with `python course_tools/build_course.py`. Do not edit generated ZIPs or HTML by hand.
- Run `python course_tools/check_course.py` after changes. Run the affected lessons and their documented changes too.
- Report checks that could not be run. Never call a learner study, clean installation, or cloud deployment tested unless it happened.
