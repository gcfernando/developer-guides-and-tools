---
layout: default
title: "Machine Learning Practical Lessons — Glossary"
description: "Look up data, model training, evaluation and service terms with links to worked Python exercises."
permalink: /examples/machine-learning/ml-practical-lessons/glossary/
---

# 🔎 Searchable glossary

[← Back to the workbook](Data-Science-and-Machine-Learning.md#contents)

Press **Ctrl+F** on Windows or Linux, or **Command+F** on a Mac. Search for the term you saw in a lesson. The last column opens a worked example.

## 📄 Files and data

| Term | Meaning | Try it |
| --- | --- | --- |
| **CSV** | A text file of rows and columns. In the delivery exercise, each row holds one delivery. | [First prediction](Data-Science-and-Machine-Learning.md#your-first-prediction) |
| **Terminal** | An app for typing and running commands such as `python lesson.py`. | [Setup](SETUP.md) |
| **Virtual environment** | A folder with its own installed Python packages. The setup creates one called `.venv`. | [Setup](SETUP.md) |
| **Input / feature** | A value the app already knows, such as distance or parcel weight. | [First prediction](Data-Science-and-Machine-Learning.md#your-first-prediction) |
| **Target / label** | The answer you want the model to learn, such as measured minutes or whether a delivery was urgent. | [First prediction](Data-Science-and-Machine-Learning.md#your-first-prediction) |
| **Prediction** | The model’s answer for a particular input. | [First prediction](Data-Science-and-Machine-Learning.md#your-first-prediction) |
| **Missing value / imputation** | A field can be blank. Imputation is a rule for estimating the blank when filling it is appropriate. Learn that rule from training data. | [Missing values](Data-Science-and-Machine-Learning.md#1-3-1-handle-missing-values) |
| **Outlier** | An unusual value worth investigating. Check its source before deciding whether to keep, correct, or set it aside. | [Outliers](Data-Science-and-Machine-Learning.md#spot-check-and-handle-an-outlier) |
| **Scaling** | Changing the range or units of a number before a model uses it. A new value can lie outside the training range. | [Min-Max Scaling](Data-Science-and-Machine-Learning.md#normalization-min-max-scaling) |
| **Encoding** | Turning categories, such as delivery zones, into numbers the model can use. | [One-Hot Encoding](Data-Science-and-Machine-Learning.md#one-hot-encoding-for-unordered-categories) |

## 🧪 Training and checks

| Term | Meaning | Try it |
| --- | --- | --- |
| **Training / validation / test** | Learn from training rows, select settings on validation rows, and check the chosen model on separate test rows. | [Split selection](Data-Science-and-Machine-Learning.md#lesson-442) |
| **Data leakage** | A model or its selection process sees information reserved for testing or unavailable when making a prediction. | [Split selection](Data-Science-and-Machine-Learning.md#lesson-442) |
| **Stratification** | Keeping roughly the same proportions of classes in each split. | [Stratified Sampling](Data-Science-and-Machine-Learning.md#stratified-sampling) |
| **Group split** | Keeping the rows for each customer together when you want to test on unseen customers. | [Split selection](Data-Science-and-Machine-Learning.md#lesson-442) |
| **Chronological split** | Learning on earlier dates and checking on later ones. | [Split selection](Data-Science-and-Machine-Learning.md#lesson-442) |
| **Cross-validation** | Taking turns using different subsets for validation and the rest for training. Fit any preparation step again inside each training subset. | [Compare transformations](Data-Science-and-Machine-Learning.md#which-technique-should-you-use) |
| **Baseline** | A simple reference, such as predicting the training median on every delivery. | [Regression evaluation](Data-Science-and-Machine-Learning.md#lesson-446) |
| **Overfitting** | Learning details that help on training rows but hurt on separate rows. | [Validation curve](Data-Science-and-Machine-Learning.md#lesson-443) |
| **Confusion matrix** | A count table comparing the model’s class with the real class. One cell counts urgent deliveries the model missed. | [Confusion Matrix](Data-Science-and-Machine-Learning.md#confusion-matrix) |
| **Precision / recall** | Precision asks what fraction of alerts were correct. Recall asks what fraction of actual urgent orders the model caught. | [Rare-event cutoff](Data-Science-and-Machine-Learning.md#lesson-444) |
| **False alarm / missed urgent order** | An alert for a regular delivery, or an urgent delivery that received no alert. | [Confusion Matrix](Data-Science-and-Machine-Learning.md#confusion-matrix) |
| **Cutoff / threshold** | The score at which the model starts raising an alert. | [Rare-event cutoff](Data-Science-and-Machine-Learning.md#lesson-444) |
| **ROC curve** | A chart of the fraction of urgent orders caught versus the fraction of regular orders that raise false alarms, as the cutoff changes. | [ROC Curve](Data-Science-and-Machine-Learning.md#roc-curve) |
| **Calibration / Brier score** | Calibration checks whether predicted chances agree with observed frequencies. Brier score measures mean squared probability error. | [Calibration](Data-Science-and-Machine-Learning.md#lesson-445) |
| **MAE / RMSE** | Measures of numerical error in the original units. MAE averages absolute errors. RMSE gives larger errors more weight. | [Regression evaluation](Data-Science-and-Machine-Learning.md#lesson-446) |

## 🚚 Using a model

| Term | Meaning | Try it |
| --- | --- | --- |
| **Pipeline** | A sequence of preparation steps and a model. It applies the learned preparation to new rows. | [Capstone](Data-Science-and-Machine-Learning.md#lesson-447) |
| **API / HTTP status** | An API accepts requests. Its HTTP status can report success (200), or explain a problem such as invalid fields (422 in the capstone). | [Capstone](Data-Science-and-Machine-Learning.md#lesson-447) |
| **Drift / monitoring** | Drift is change over time in inputs or their relationship to outcomes. Monitoring checks new data and tracks errors once measured outcomes arrive. | [Capstone](Data-Science-and-Machine-Learning.md#lesson-447) |
