from db_operations import add_expense, view_expenses, calculate_total, delete_expense

def add_expense_cli():
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric amount.")

    print("\nSelect Category:")
    print("1. Food")
    print("2. Transport")
    print("3. Rent")
    print("4. Shopping")
    print("5. Others")

    choice = input("Choose option: ")

    if choice == "1":
        category = "Food"
    elif choice == "2":
        category = "Transport"
    elif choice == "3":
        category = "Rent"
    elif choice == "4":
        category = "Shopping"
    elif choice == "5":
        category = input("Enter custom category: ")
    else:
        print("Invalid category.")
        return

    add_expense(amount, category)
    print("Expense added successfully.")

def view_expenses_cli():
    rows=view_expenses()
    if not rows:
        print("No expenses recorded yet.")
        return
    print("\nRECORDED EXPENSES:")
    for row in rows:
        print(f"{row[0]}. {row[2]} | amount: {row[1]} | category: {row[3]}")


def calculate_total_cli():
    total=calculate_total()
    print(f"Total Expenses: {total}")

def delete_expense_cli():
    rows=view_expenses()
    if not rows:
        print("No expenses yet.")
        return
    view_expenses_cli()

    while True:
        try:
            choice = int(input("Enter the ID of the expense to delete:"))
            delete_expense(choice)
            print("Expense Deleted Successfully.")
            break
        except ValueError:
            print("Please enter a valide number.")


def main():
    print("EXPENSE TRACKER APPLICATION")

    while True:
        print("\nExpense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expense")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense_cli()
        elif choice == "2":
            view_expenses_cli()
        elif choice == "3":
            calculate_total_cli()
        elif choice == "4":
            delete_expense_cli()
        elif choice == "5":
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()        