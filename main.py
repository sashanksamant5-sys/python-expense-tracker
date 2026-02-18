import json
from datetime import datetime
expenses=[]
def add_expense():
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount<=0:
                print("Amount Must Be Greater Then 0 ")
                continue
            break
        except ValueError:
            print("Invalide Input. Please enter the numeric amount.")

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
    
    current_time=datetime.now().strftime("%d-%m-%Y | %H:%M:%S")
    print(f"Expense Added: {current_time} | {amount} | {category}")
        
    expense = {
        "time": current_time ,
        "amount" : amount,
        "category" : category
        }

    expenses.append(expense)
    save_expenses()
    print("Expense is added successfully")
    

def view_expense():
    if not expenses:
        print("No records founded")
        return
    print("\nRECORDED EXPENSES:")
    for index, expense in enumerate(expenses,start=1):
        print(f"{index}.{expense['time']} | amount:{expense['amount']} | category: {expense['category']}")

def calculate_total(expenses):
    if not expenses:
        print("No Expenses Recorded yet")
    total = 0
    total = sum(expense['amount'] for expense in expenses)
    print("Total Expense:",total)

def delete_expenses():
    if not expenses:
        print("No Expenses Recorded yet.")
        return
    
    view_expense()

    while True:
        try:
            choice=int(input("Enter the number of expense to delete:"))
            if 1<=choice<=len(expenses):
                removed = expenses.pop(choice - 1)
                save_expenses()
                print("deleted:",removed["category"], "-", removed["amount"])
                break
            else:
                print("Invalid Input. Try again.")

        except ValueError:
            print("Please Enter a Valide Number.")

def save_expenses():
    with open("expenses.json","w") as file:
        json.dump(expenses,file,indent=4)

def load_expenses():
    global expenses
    try:
        with open("expenses.json","r") as file:
            expenses=json.load(file)
    except FileNotFoundError:
        expenses=[]
def main():
    load_expenses()
    print("EXPENSE TRACKER APPLICATION")

    while True:
        print("\nExpense tracker Menu")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. view total expense")
        print("4. Delete expense")
        print("5. Exit")

        choice = input("Enter your choice:")

        if choice == "1":
            add_expense()

        elif choice == "2":
           # print("View Expense selected")
           view_expense()

        elif choice == "3":
            calculate_total(expenses)

        elif choice == "4":
            delete_expenses()

        elif choice == "5":
            print("Exiting application:")
            break

        elif choice == "5":
            delete_expenses()

        else:
            print("Invalid choice.Try again.")

if __name__ == "__main__":
    main()

