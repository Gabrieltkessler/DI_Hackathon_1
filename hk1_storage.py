import json
import os

FILE_PATH = "hk1_expenses.json"


def load_expenses():
    #IF NO FILE, RETURN EMPTY LIST
    if not os.path.exists(FILE_PATH):
        return []

    #READ FILE
    with open(FILE_PATH, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_expenses(expenses):
    #WRITE TO JSON FILE
    with open(FILE_PATH, "w") as file:
        json.dump(expenses, file, indent=4)