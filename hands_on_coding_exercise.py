"""
Week 3 Task: Hands-On Coding Exercise Documentation
Mini Project: Daily Expense Tracker

A beginner-friendly command-line program that lets a user add expenses,
view recorded expenses, and calculate the total. It includes basic input
validation and a simple menu.

Run:
    python hands_on_coding_exercise.py
"""

def read_amount(prompt):
    """Read a positive numeric amount, retrying when input is invalid."""
    while True:
        raw_value = input(prompt).strip()
        try:
            amount = float(raw_value)
            if amount <= 0:
                print("Please enter an amount greater than zero.")
                continue
            return round(amount, 2)
        except ValueError:
            print("Invalid amount. Enter a number, such as 25 or 25.50.")


def add_expense(expenses):
    """Collect one expense and append it to the in-memory list."""
    name = input("Enter expense name: ").strip()
    if not name:
        print("Expense name cannot be empty.")
        return

    amount = read_amount("Enter amount (₹): ")
    expenses.append({"name": name, "amount": amount})
    print(f"Added: {name} — ₹{amount:.2f}")


def view_expenses(expenses):
    """Display all saved expenses for the current session."""
    if not expenses:
        print("No expenses have been added yet.")
        return

    print("\nRecorded Expenses")
    print("-----------------")
    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense['name']}: ₹{expense['amount']:.2f}")
    print(f"Total expenses: ₹{calculate_total(expenses):.2f}")


def calculate_total(expenses):
    """Return the sum of all recorded expense amounts."""
    return round(sum(expense["amount"] for expense in expenses), 2)


def main():
    """Run the interactive menu until the user chooses to exit."""
    expenses = []

    while True:
        print("\nDaily Expense Tracker")
        print("1. Add an expense")
        print("2. View expenses and total")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            print(f"Session total: ₹{calculate_total(expenses):.2f}")
            print("Thank you for using the Daily Expense Tracker.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
