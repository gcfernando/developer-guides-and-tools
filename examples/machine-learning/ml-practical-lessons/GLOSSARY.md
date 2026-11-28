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


## Small numbers and shapes

| Word | Simple meaning |
| --- | --- |
| Mean | Add the values and divide by their count. The mean of 2, 4 and 6 is 4. |
| Median | Sort values and find the middle. The median of 1, 2 and 90 is 2. With an even count, average the middle two. |
| Mode | A most common value. Ties need a stated rule. |
| Percentage | A share out of 100. Two out of ten is 20%. |
| Distribution | How values are spread across a range. |
| Standard deviation | A measure of how far values spread around their mean. |
| Quartile / IQR | Quartiles divide sorted values into quarters. IQR is the gap between the lower and upper quarters. |
| Correlation | A measure of how two values move together. It does not prove a cause. |
| Row / column | A row is one record across a table. A column is one kind of fact down it. |
| Array / matrix / tensor | Arrays hold values in positions. A matrix has rows and columns. Tensor is a general word for arrays with several dimensions. |
| Shape | The size along each array direction. Shape (6, 8) means six rows and eight values per row. |
| Vector | One list of numbers. A message embedding is one such list. |

## Code and learning words

| Word | Simple meaning |
| --- | --- |
| Variable | A name holding a value, such as distance = 4. |
| String | Text in code, often written in quotes. An ID can be a string even if it contains digits. |
| Function / method | Named steps that do a job. A method belongs to an object, as in model.predict. |
| Package | Extra Python tools. Install a package, then import the part you need. |
| DataFrame / pandas | A DataFrame is a table in Python. pandas supplies the table tools. |
| CSV / JSON | CSV is a text table. JSON is text with named fields, often used in requests. |
| Fit | Learn model or preparation values from training examples. |
| Transform | Apply a preparation rule. Use the rule learned during training. |
| Model setting / hyperparameter | A choice controlling learning, such as a tree's allowed depth. |
| Regularization / alpha | A penalty discouraging some complex fits or large weights. Alpha controls its strength in Ridge and Lasso. Feature units can affect the penalty. |
| Coefficient / weight | A learned value that changes how an input contributes to a model result. |
| Loss | A number measuring mistakes during learning. The model tries to reduce it. |
| Optimizer / gradient | An optimizer changes learned values. A gradient describes a direction of change for a loss. |
| Epoch | One pass through the training data. |
| Embedding | A list of numbers representing an item. It may be hand-built or learned. |
| Token / vocabulary | A token is a text piece, such as a word. A vocabulary is the set of pieces known by the text process. |
| Pseudo-label | A model's guessed training answer. It is not a confirmed fact. |
| Silhouette | A score about group separation under a chosen distance rule. It does not prove business usefulness. |
| Probability | A stated chance, between 0 and 1. It is not a promise for one event. |
| R squared | A score comparing squared errors with a mean-answer benchmark on the same check rows. Zero matches that benchmark; negative can be worse. |
| Residual | Actual value minus predicted value. Positive delivery residuals mean the guess was too short. |
| Metadata / data dictionary | Metadata is notes about data or a model. A data dictionary explains each field and its units. |
| API / endpoint / port | An API lets programs exchange requests and replies. An endpoint is a particular route, such as /predict. A port is a numbered connection point, such as 8000. |
| Artifact / inference | An artifact is a saved output, such as a model file. Inference means using a trained model to make predictions. |
| Local / cloud | Local runs on your computer. Cloud runs on another service's computers. A local test does not publish a service. |
| Policy / return / exploration | A policy chooses an action. Return adds rewards over a route. Exploration tries actions to learn about them. |

Read [Python basics](PYTHON-BASICS.md) for the symbols, and [Extra topics](ELECTIVES.md) for advanced names. You do not need to learn them all before the first lesson.
