#Build the Expense Manager (CRUD logic)
from hk1_models import Expense
from hk1_storage import load_expenses, save_expenses
import uuid

class ExpenseManager:
    def __init__(self):
        self.expenses = load_expenses()

    #CREATE
    def add_expense(self, amount, category, description, date):
        expense = Expense(
            str(uuid.uuid4()),
            amount,
            category,
            description,
            date)

        self.expenses.append(expense.to_dict())
        save_expenses(self.expenses)

    #READ
    def get_all_expenses(self):
        return self.expenses

    #DELETE
    def delete_expense(self, expense_id):
        self.expenses = [
            e for e in self.expenses if e["expense_id"] != expense_id
        ]
        save_expenses(self.expenses)

    #CLEAR EXPENSES
    def clear_expenses(self):
        self.expenses = []
        save_expenses(self.expenses)

    #UPDATE
    def update_expense(self, expense_id, field, new_value):
        for expense in self.expenses:
            if expense["expense_id"] == expense_id:
                expense[field] = new_value
        save_expenses(self.expenses)

    #API REQUEST
    def get_total_expenses(self):
        total = 0
        for expense in self.expenses:
            total += expense["amount"]
        return total