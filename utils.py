def get_amount():
    while True:
        try:
            amount = float(input("Enter amount: ₹"))

            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                return amount

        except ValueError:
            print("Please enter a valid amount.")


def get_category():
    categories = [
        "Food",
        "Transport",
        "Shopping",
        "Education",
        "Entertainment",
        "Other"
    ]

    print("\nCategories:")

    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")

    while True:
        try:
            choice = int(input("Choose category: "))

            if 1 <= choice <= len(categories):
                return categories[choice - 1]
            else:
                print("Please choose a valid option.")

        except ValueError:
            print("Please enter a number.")