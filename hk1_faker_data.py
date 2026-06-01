from faker import Faker
import random
from hk1_manager import ExpenseManager

fake = Faker()

CATEGORIES = ["Food", "Transport", "Bills", "Entertainment", "Shopping"]

def generate_fake_expenses(n=10):
    manager = ExpenseManager()

    for _ in range(n):
        amount = round(random.uniform(5,300),2)
        category = random.choice(CATEGORIES)
        description = fake.sentence()
        date = fake.date()

        manager.add_expense(amount, category, description, date)

    print(f"{n} fake expenses generated successfully.")

