from expense import Expense
from storage import save_expenses


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

##-------------------------------------------------------------------------------------------------------------------------------------

## Budget -----------------------------------------------------------------------------------------------------------------------------
def view_budget(budget):
    #check if there is a budget to show
    if not budget:
        print("No budget have been set yet.")
        return
    
    print (f"\nYour Current Budget is: {budget}")

def set_budget():
    while True:
        try:
            amount = float(input("Enter your monthly budget amount: $"))
            if amount <= 0:
                print("Budget must be greater than zero.")
                continue
            return amount
        except ValueError:
            print("Please enter a valid number.")
            continue

def remove_budget(budget):
    pass

## -------------------------------------------------------------------------------------------------------------------------------------