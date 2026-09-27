def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total


def category_analysis(expenses):
    categories = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    return categories


def show_analysis(expenses):
    if not expenses:
        print("\nNo expenses available for analysis.")
        return

    total = calculate_total(expenses)
    categories = category_analysis(expenses)

    print("\n===== EXPENSE ANALYSIS =====")
    print(f"Total Spending: ₹{total:.2f}")

    print("\nSpending by Category:")

    for category, amount in categories.items():
        percentage = (amount / total) * 100
        print(f"{category}: ₹{amount:.2f} ({percentage:.1f}%)")