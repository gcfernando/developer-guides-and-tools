---
layout: default
title: "Machine Learning Practical Lessons — Python Workbook"
description: "Learn data preparation, model evaluation and local prediction services with a guided Python workbook, synthetic datasets and downloadable lessons."
permalink: /examples/machine-learning/ml-practical-lessons/guide/
---

# Machine learning practical lessons

Choose a starting point by what you can explain, not by how many files you have run. Several lesson numbers share a script but ask different questions. Each teaching note now names its decision, needed prior skill, worked example, input/output, limits and new application task.

| Your immediate goal | Start with | Evidence you can produce |
| --- | --- | --- |
| Understand a prediction without code | Start here and paper practice | Explain a new input, estimate and measured answer. |
| Run and modify a first model | Setup, Python basics and 002 | Save an edit and explain the changed result. |
| Build a checked project | The required learning path | Compare with a baseline and justify a fair check. |
| Explore an advanced method | Its Extra topics readiness task | Trace input to output and name an unsuitable case. |
| Demonstrate independent application | The Wine project after guided work | Hand over your own reproducible procedure and limitations. |

**Check your next choice.** You can run a script but cannot explain why it reuses a saved scaler. Return to the preparation lesson and trace a new row before collecting more algorithm names. Record execution and explanation as different achievements.

[Developer guides and tools](https://gcfernando.github.io/developer-guides-and-tools/repository/) · [All examples](https://gcfernando.github.io/developer-guides-and-tools/examples/) · [Machine learning path](https://gcfernando.github.io/developer-guides-and-tools/learning-paths/machine-learning/)

Learn machine learning one small step at a time. Start with a table and a prediction you can calculate on paper. Later, use Python to learn from old deliveries, check mistakes, and try a local prediction service.

For a reading view with course navigation, open the [browser course overview](https://gcfernando.github.io/developer-guides-and-tools/examples/machine-learning/ml-practical-lessons/README.html). It links to the readable learning path and exercises. The [Markdown source](https://github.com/gcfernando/developer-guides-and-tools/blob/main/examples/machine-learning/ml-practical-lessons/README.md) remains available for readers who prefer GitHub or want to edit the text. Use Library home or All resources in the browser reader to return to the wider collection.

[Start here](START-HERE.md) · [Follow the learning path](https://gcfernando.github.io/developer-guides-and-tools/examples/machine-learning/ml-practical-lessons/LEARNING-PATH.html) · [Read the workbook](Data-Science-and-Machine-Learning.md) · [Set up Python](SETUP.md) · [Word list](GLOSSARY.md)

## Start here

1. Open [Start here](START-HERE.md). It explains rows, columns, a prediction, and basic computer words.
2. Choose the ideas route or the Python route. The ideas route needs no installation.
3. For Python, follow [Setup](SETUP.md), then [Python basics](https://gcfernando.github.io/developer-guides-and-tools/examples/machine-learning/ml-practical-lessons/PYTHON-BASICS.html). Use the same active environment for every command.
4. Follow [Your learning path](https://gcfernando.github.io/developer-guides-and-tools/examples/machine-learning/ml-practical-lessons/LEARNING-PATH.html). Tick a box only when you can explain its check.
5. Finish the guided delivery project. Then try the [independent project](https://gcfernando.github.io/developer-guides-and-tools/examples/machine-learning/ml-practical-lessons/INDEPENDENT-PROJECT.html) with a real, separately sourced table.

For offline reading, open `START-HERE.html`. Keep the complete course folder together. All main guides have readable HTML copies. Each lesson ZIP also includes `README.html`.

## What is included

| Material | Purpose |
| --- | --- |
| Markdown and HTML workbooks | Two reading formats for the same course, with explanations, worked outputs and lesson links |
| 447 numbered entries | 24 Core, 380 Practice and 43 Reference entries. Some numbers ask different questions about the same exercise. They are not 447 separate projects. |
| 448 ZIP downloads | The numbered lessons plus a separate [train-and-test example](sample_code_folder/train-and-test.zip) |
| `sample_code_folder/` | Lesson archives containing scripts, sample data, requirements and instructions |
| `workbook-figures/` | Diagrams and charts with readable mobile variants, text explanations and source-backed value tables |
| `lessons/` | Editable source files used to build the lesson ZIPs. Learners can use the ZIPs instead. |
| `projects/wine/` | A real-data independent project with a starter script, separate final answers and source credit. |
| [Practice](https://gcfernando.github.io/developer-guides-and-tools/examples/machine-learning/ml-practical-lessons/PRACTICE.html), [Project choices](https://gcfernando.github.io/developer-guides-and-tools/examples/machine-learning/ml-practical-lessons/PROJECT-CHOICES.html), and [Extra topics](https://gcfernando.github.io/developer-guides-and-tools/examples/machine-learning/ml-practical-lessons/ELECTIVES.html) | Questions with explained answers, project worksheets and help for harder topics. |
| [Lesson coverage](coverage.csv) | Lesson IDs, tracks, sample files, expected results and shared-exercise mappings |
| [Core requirements](requirements-core-tested.txt) and [recorded versions](tested-package-versions.csv) | The supplied dependency recipe and environment record |

## Follow the practical route

The path teaches the needed skills before the final project. You will define a question, keep a fair check, find data problems, prepare inputs, compare a simple guess with a model, spot memorizing, and inspect mistakes. The [guided delivery project](Data-Science-and-Machine-Learning.md#lesson-447) connects the steps. Its service runs on your computer. Stop it with Ctrl+C when finished.

Finishing the ideas route means you can ask useful questions about a project. Finishing the Python route means you can build and explain a small checked project. Reading or copying outputs alone does not mean you have mastered ML.

## Requirements and verification limits

The supplied setup guide records testing with Python 3.12.14 on Linux. Windows and macOS instructions are provided, but clean installs on those platforms are unverified. Common packages are pinned in the core requirements; individual lessons may need additional packages. Reading the workbook needs no Python installation.

The numbered lessons use made-up data. The independent project uses real UCI Wine data with credit and its licence. Example outputs do not prove that a model works for a real service. Extra cloud steps need an approved account and cost checks. Load only Joblib model files you made or trust, because loading one can run code.

No lesson scripts are executed by the repository's standard documentation build. Keep generated models, extracted practice folders and personal data in a separate working copy. Check the lesson README before running it.

## For the course author

Use [Teaching](https://gcfernando.github.io/developer-guides-and-tools/examples/machine-learning/ml-practical-lessons/TEACHING.html) for the lesson template, learner study and release checks. Run `python course_tools/build_course.py` to rebuild pages and ZIPs, then `python course_tools/check_course.py` to check the result. [The original review](https://gcfernando.github.io/developer-guides-and-tools/examples/machine-learning/ml-practical-lessons/course-review/report.html) describes the earlier course. [The response log](course-review/implementation-status.csv) records changes and any human checks still needed.
