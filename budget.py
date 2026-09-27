def set_budget():
    while True:
        try:
            budget = float(input("Enter your monthly budget: ₹"))

            if budget <= 0:
                print("Budget must be greater than zero.")
            else:
                return budget

        except ValueError:
            print("Please enter a valid number.")


def check_budget(budget, total_expense):
    remaining = budget - total_expense

    print("\n===== BUDGET STATUS =====")
    print(f"Budget: ₹{budget:.2f}")
    print(f"Spent: ₹{total_expense:.2f}")

    if remaining >= 0:
        print(f"Remaining: ₹{remaining:.2f}")
    else:
        print(f"Over budget by: ₹{abs(remaining):.2f}")