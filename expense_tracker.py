
expenses = []

def add_expense():
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        description = input("Enter description: ")

        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }

        expenses.append(expense)
        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid amount.")

def view_expenses():
    if not expenses:
        print("No expenses found.")
        return

    for number, expense in enumerate(expenses, start=1):
        print(
            number,
            expense["category"],
            "Rs.", expense["amount"],
            "-", expense["description"]
        )

def show_total():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("Total spending: Rs.", total)

while True:
    print("\n--- Personal Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        show_total()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")
