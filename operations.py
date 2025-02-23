from expense import Expense
from storage import save_expenses
from budget import Budget


## Expenses --------------------------------------------------------------------------------------------------------------------------
def view_expenses(expenses):
    # Check if we have any expenses to show
    if not expenses:
        print("No expenses recorded yet!")
        return
    
    # Print header for our expense table
    print("\nYour Expenses:")
    print("Index ID\t\tDate\t\tAmount\t\tCategory")
    print("-" * 80)  # Print a dividing line
    
    # Loop through each expense and print it nicely formatted
    index=0
    for expense in expenses:
        print(f"{index}\t\t\t{expense.date}\t${expense.amount:.2f}\t\t{expense.category}")
        index += 1
        # The :.2f means "show 2 decimal places"

    print ("\nTotal expenses: ${:.2f}".format(sum(expense.amount for expense in expenses)))

def add_new_expense():
    # This just uses our Expense class's from_user_input method
    return Expense.from_user_input()

def delete_expense(expenses, expense_index):
    # This just uses our Expense class's from_user_input method
    return expenses.pop(expense_index)

def handle_add_expense(expenses):
    expense = add_new_expense()
    if expense:
        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added successfully!")
    else:
        print("Expense addition cancelled.")

def analyze_expenses(expenses, budget):
    if not expenses:
        print("\nNo expenses to analyze.")
        return

    # Calculate total expenses and category breakdown
    total_spent = sum(expense.amount for expense in expenses)
    categories = {}
    
    for expense in expenses:
        if expense.category not in categories:
            categories[expense.category] = 0
        categories[expense.category] += expense.amount

    # Display analysis
    print("\n=== Expense Analysis ===")
    print(f"Total Spent: ${total_spent:.2f}")
    
    if budget:
        budget_remaining = budget - total_spent
        print(f"Monthly Budget: ${budget:.2f}")
        print(f"Budget Remaining: ${budget_remaining:.2f}")
        print(f"Budget Status: {'Over budget' if budget_remaining < 0 else 'Under budget'}")
    
    print("\nSpending by Category:")
    for category, amount in categories.items():
        percentage = (amount / total_spent) * 100
        print(f"{category}: ${amount:.2f} ({percentage:.1f}%)")

##-------------------------------------------------------------------------------------------------------------------------------------

## Budget -----------------------------------------------------------------------------------------------------------------------------
def view_budget(budget):
    #check if there is a budget to show
    if not budget:
        print("No budget have been set yet.")
        return
    
    print (f"\nYour Current Budget is: ${budget:.2f}")

def set_budget():
    return Budget.from_user_input()

def remove_budget(budget):
    pass

## -------------------------------------------------------------------------------------------------------------------------------------