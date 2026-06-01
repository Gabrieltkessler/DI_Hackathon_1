#Interactive CLI menu

from hk1_manager import ExpenseManager
from hk1_faker_data import generate_fake_expenses
from hk1_api_service import get_exchange_rate

def show_menu():
    print("\n===== EXPENSE TRACKER =====\n")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Generate Fake Expenses")
    print("6. Clear All Expenses")
    print("7. Show Total in EUR")
    print("0. Exit")
    print("====================================")

def main():
    manager = ExpenseManager()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        #ADD EXPENSE
        if choice == "1":
            amount = float(input("Enter the amount: "))
            category = input("Enter the category: ")
            description = input("Enter the description: ")
            date = input("Enter the date (YYYY-MM-DD): ")

            manager.add_expense(amount, category, description, date)
            print("Expense successfully added!")

        #VIEW EXPENSES
        elif choice == "2":
            expenses = manager.get_all_expenses()

            if not expenses:
                print("No expenses found.")
            else:
                for e in expenses:
                    print(e)

        #UPDATE EXPENSE
        elif choice == "3":
            expense_id = input("Enter the expense ID: ")
            field = input("What to update (amount/category/description/date): ")
            new_value = input("Enter the new value: ")

            #CONVERT AMOUNT IF NEEDED
            if field == "amount":
                new_value = float(new_value)

            manager.update_expense(expense_id, field, new_value)
            print("Expense successfully updated!")

        #DELETE EXPENSE
        elif choice == "4":
            expense_id = input("Enter the expense ID: ")
            manager.delete_expense(expense_id)
            print("Expense successfully deleted!")

        #ADD FAKE EXPENSES
        elif choice == "5":
            n = int(input("How many fake expenses?: "))
            generate_fake_expenses(n)

            manager = ExpenseManager()

        #CLEAR EXPENSES
        elif choice == "6":
            confirm = input("Are you sure? (yes/no): ")

            if confirm.lower() == "yes":
                manager.clear_expenses()
                print("All expenses cleared.")
            else:
                print("Cancelled.")

        #EXCHANGE RATE API REQUEST
        elif choice == "7":
            total = manager.get_total_expenses()
            rate = get_exchange_rate("USD", "EUR")

            if rate:
                print(f"Total in EUR: €{total * rate:.2f}")
            else:
                print("Failed to fetch exchange rate.")

        #EXIT
        elif choice == "0":
            print("Thank you for using this program!")
            break
        else:
            print("Invalid choice. Please Try again.")

if __name__ == "__main__":
    main()
