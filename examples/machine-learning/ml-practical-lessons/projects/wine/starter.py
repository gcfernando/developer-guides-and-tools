"""Read the independent-project files. Add your own model in a copy of this file."""

from pathlib import Path
import pandas as pd

FOLDER = Path(__file__).resolve().parent


def main():
    training = pd.read_csv(FOLDER / "training.csv")
    validation = pd.read_csv(FOLDER / "validation.csv")
    test_inputs = pd.read_csv(FOLDER / "test_inputs.csv")
    features = [name for name in training.columns if name not in ("row_id", "wine_type")]
    print("Rows to learn:", len(training))
    print("Rows to choose:", len(validation))
    print("Rows for the final check:", len(test_inputs))
    print("Input fields:", features)
    print("Answer field: wine_type. Its values 0, 1 and 2 are category names.")
    print("Copy this file to my_model.py. Add a baseline, one model and a validation check.")
    print("Keep instructor/test_answers.csv closed until your model choice is fixed.")


if __name__ == "__main__":
    main()
