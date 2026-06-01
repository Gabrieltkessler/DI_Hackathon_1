# builing out the expense class

class Expense:
    def __init__(self, expense_id, amount, category, description, date):
        self.expense_id = expense_id
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date

    def to_dict(self):
        return {
            "expense_id": self.expense_id,
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date
        }

    def __str__(self):
        return(
            f"ID: {self.expense_id} | "
            f"Amount: {self.amount} | " 
            f"Category: {self.category} | "
            f"Description: {self.description} | "
            f"Date: {self.date}"
        )
