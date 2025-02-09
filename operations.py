from expense import Expense

def view_expenses(expenses):
    # Check if we have any expenses to show
    if not expenses:
        print("No expenses recorded yet!")
        return
    
    # Print header for our expense table
    print("\nYour Expenses:")
    print("Date\t\tAmount\t\tCategory")
    print("-" * 40)  # Print a dividing line
    
    # Loop through each expense and print it nicely formatted
    for expense in expenses:
        print(f"{expense.date}\t${expense.amount:.2f}\t\t{expense.category}")
        # The :.2f means "show 2 decimal places"

def add_new_expense():
    # This just uses our Expense class's from_user_input method
    return Expense.from_user_input()