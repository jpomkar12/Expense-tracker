def add_expense(expenses: list):
    """prompt for an amount and category, add the expense to the list."""
    try:
        amount = float(input("Amount :"))
    except ValueError:
        print("Invalid Input")
        return
    category = input("Category :")
    expense = {"amount": amount, "category": category}
    expenses.append(expense)

def list_expenses(expenses):
    """Print every expense with category using enumerate """
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense["category"]}: ${expense["amount"]:.2f}")

def main():
    """Run the add/list/quit menu loop."""
    expenses = []           # the in-memory list lives here
    while True:
        choice = input("(a)dd, (l)ist, (q)uit: ")
        if choice == "a":
            add_expense(expenses)
        elif choice == "l":
            list_expenses(expenses)
        elif choice == "q":
            break
        else:
            print("Unknown option")


main()

    
    

