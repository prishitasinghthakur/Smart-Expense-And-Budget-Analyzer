# Smart Expense and Budget Analyzer

## 1. Project Overview

Smart Expense and Budget Analyzer is a Python-based application designed to help users manage and understand their expense.

The application allows users to enter their expenses, organize them into categories, set a budget, check their budget status, and analyse their spending.

The expense and budget data are stored only while the program is running. When the program is started again, it begins with a blank expense list and a new budget.

## 2. Features

- Add new expenses
- Categorize expenses into:
  - Food
  - Transport
  - Shopping
  - Education
  - Entertainment
  - Other
- View all expenses
- Set a budget
- Check remaining budget
- Detect when spending exceeds the budget
- Calculate total spending
- Analyse spending category-wise
- Calculate the percentage of spending in each category
- Validate user inputs and handle invalid entries
- Start with fresh data every time the application is run

## 3. Technologies and Tools Used

### Programming Language
- Python 3

### Concepts Used
- Object-Oriented Programming
- Classes and Objects
- Functions
- Lists
- Dictionaries
- Loops
- Conditional Statements
- Exception Handling
- Input Validation
- Modular Programming

### Tools
- Visual Studio Code
- Git
- GitHub

## 4. Project Structure

Smart-Expense-Tracker/
│

├── main.py

├── expense.py

├── budget.py

├── analyzer.py

├── utils.py

├── README.md

├── statement.md


### Description of Files

- **main.py** – Controls the main menu and connects all modules.
- **expense.py** – Defines the Expense class and manages expense information.
- **budget.py** – Handles budget setting and budget status checking.
- **analyzer.py** – Calculates total expenses and performs category-wise analysis.
- **utils.py** – Handles user input and input validation.
- **README.md** – Contains project documentation.
- **statement.md** – Contains the project problem statement and scope.

## 5. Installation and Setup

### Step 1: Install Python

Install **Python 3** on your computer.

Check whether Python is installed by opening the terminal and running:

"python --version"

### Step 3: Run the Project

Open the terminal inside the project folder and run:

"python main.py"

The main menu will appear in the terminal.

## 6. How to Use the Application

After running the program, the following menu is displayed:

1. Add Expense
2. View Expenses
3. Set Budget
4. Check Budget
5. Expense Analysis
6. Exit

Select an option by entering its corresponding number.


To add an expense:

```text
Enter your choice: 1### Example

Enter amount: ₹500
Choose category: 1
Enter description: Lunch
```

The expense will then be added to the current session.

To analyse expenses, select:

```text
5. Expense Analysis
```

The application will display the total spending and category-wise spending percentages.

## 7. Testing Instructions

The following tests can be performed to verify that the application works correctly.

### Test 1: Add Expense

- Select **Add Expense**.
- Enter a valid amount.
- Select a category.
- Enter a description.
- Check whether the expense is displayed successfully.

### Test 2: Invalid Amount

Enter an invalid value such as:

"abc"

The application should display:


"Please enter a valid number."


### Test 3: Set Budget

- Select **Set Budget**.
- Enter a positive budget amount.
- Check whether the budget is set successfully.

### Test 4: Check Budget

- Add one or more expenses.
- Set a budget.
- Select **Check Budget**.
- Verify the remaining amount or the amount over budget.

### Test 5: Expense Analysis

- Add expenses from different categories.
- Select **Expense Analysis**.
- Verify the total spending and category-wise percentages.

### Test 6: Fresh Session

- Run the program.
- Add expenses and set a budget.
- Exit the program.
- Run main.py again.

The new session should start with **no previous expenses and no previous budget**.


## 9. Conclusion

The **Smart Expense and Budget Analyzer** provides a simple way to record expenses, manage a budget, and understand spending patterns using Python.

The project demonstrates practical implementation of Python programming concepts such as functions, classes, lists, dictionaries, loops, conditional statements, exception handling, and modular programming.
