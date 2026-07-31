def grand_total(expenses: list) -> float:
    """Return the sum of all the amounts"""
    return sum(expense["amount"] for expense in expenses)


def category_totals(expenses: list[dict]) -> dict[str, float]:
    """Return a dict mapping each category to its total amount."""
    result = {}
    for expense in expenses:
        category = expense["category"]
        result[category] = result.get(category, 0) + expense["amount"]
    return result


def print_summary(expenses: list[dict]) -> None:
    """Print total expense and category wise expense"""
    if not expenses:
        print("No expenses yet")
        return
    total = grand_total(expenses)
    print(f"Total spent: ${total:.2f}")
    for category, amount in category_totals(expenses).items():
        print(f"{category} : ${amount:.2f}")

        
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
            print_summary(expenses)
        elif choice == "q":
            break
        else:
            print("Unknown option")





main()

    
    

