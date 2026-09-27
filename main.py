from expense import Expense
from budget import set_budget, check_budget
from analyzer import calculate_total, show_analysis
from utils import get_amount, get_category


def add_expense(expenses):
    print("\n===== ADD EXPENSE =====")

    amount = get_amount()
    category = get_category()

    description = input("Enter description: ")

    expense = Expense(amount, category, description)

    expenses.append(expense.to_dict())

    print("\n✓ Expense added successfully!")


def view_expenses(expenses):
    print("\n===== ALL EXPENSES =====")

    if not expenses:
        print("No expenses found.")
        return

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. ₹{expense['amount']:.2f} | "
            f"{expense['category']} | "
            f"{expense['description']}"
        )


def main():

    # Fresh data every time the program starts
    expenses = []
    budget = 0

    print("\n╔══════════════════════════════════╗")
    print("║      SMART EXPENSE TRACKER       ║")
    print("║       & BUDGET ANALYZER          ║")
    print("╚══════════════════════════════════╝")

    print("\n“Track it. Analyse it. Manage it.”")

    while True:

        print("\n==============================")
        print("           MAIN MENU")
        print("==============================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Set Budget")
        print("4. Check Budget")
        print("5. Expense Analysis")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            budget = set_budget()
            print("✓ Budget set successfully!")

        elif choice == "4":
            if budget == 0:
                print("\nPlease set your budget first.")
            else:
                total = calculate_total(expenses)
                check_budget(budget, total)

        elif choice == "5":
            show_analysis(expenses)

        elif choice == "6":
            print("\nThank you for using Smart Expense Tracker!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()