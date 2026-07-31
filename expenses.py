def grand_total(expenses: list) -> None:
    """Print the sum of all the amounts"""
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total spent: {total:.2f}")


def clean_category(raw: str) -> str:
    """Normalize a raw category string for consistent grouping."""
    raw = raw.strip().lower()
    if not raw:
        return "uncategorized"
    else:
        return raw


def add_expense(expenses: list)-> None:
    """prompt for an amount and category, add the expense to the list."""
    try:
        amount = float(input("Amount :"))
    except ValueError:
        print("Invalid Input")
        return
    category = clean_category(input("Category :"))
    expense = {"amount": amount, "category": category}
    expenses.append(expense)


def list_expenses(expenses: list)-> None:
    """Print every expense with category using enumerate """
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['category']}: ${expense['amount']:.2f}")




def main():
    """Run the add/list/quit menu loop."""
    expenses = []           # the in-memory list lives here
    while True:
        choice = input("(a)dd, (l)ist, (s)ummary, (q)uit: ").strip().lower()
        if choice == "a":
            add_expense(expenses)
        elif choice == "l":
            list_expenses(expenses)
        elif choice == "s":
            grand_total(expenses)
        elif choice == "q":
            break
        else:
            print("Unknown option")





main()

    
    

