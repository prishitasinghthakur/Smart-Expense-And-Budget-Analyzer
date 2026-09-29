# Problem Statement

Most people do not maintain a structured record of their day-to-day expenses. As a result, they are often unaware of how much they have spent in a given month, which category consumes the most money, or whether they have exceeded their intended budget until it is too late. Spreadsheet tools exist, but they are often heavier than needed for a quick, personal, single-session check of spending.

This project solves that problem by providing a simple, no-installation, no-internet, command-line tool that lets a user log expenses as they happen, set a monthly budget, and instantly see whether they are within budget, along with a category-wise breakdown of where the money went.

## Scope of the Project

- A single-user, single-session, console-based expense tracker and budget analyzer.
- Expenses are categorised under six fixed categories: Food, Transport, Shopping, Education, Entertainment, and Other.
- Data is held in memory (Python lists) for the duration of one program run; persistent storage (file/database) is out of scope for this   version and is listed as a future enhancement.
- No graphical interface — the application runs entirely in the terminal.

## Target Users

- Students and young professionals who want a quick, no-frills way to track daily spending.
- Anyone who wants to check their spending against a monthly budget without setting up a spreadsheet or installing an app.
- Learners studying Python who want to see functions, modules, OOP, and exception handling applied in a small real-world project.

## High-Level Features

1. **Expense Management** — add and view expenses with amount, category, and description.
2. **Budget Management** — set a monthly budget and check current spending against it.
3. **Expense Analysis** — view total spending and a percentage-wise, category-wise breakdown.
4. **Input Validation** — every numeric input is validated, with the program re-prompting on invalid entries instead of crashing.
