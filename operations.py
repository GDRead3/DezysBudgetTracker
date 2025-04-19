from datetime import datetime
from expense import Expense
from budget import Budget
from storage import save_expenses
from validation import validate_date, validate_amount, validate_description, validate_budget_amount

"""
Dezy's Budget Tracker - Operations Module

This module contains the core functionality for the budget tracking application.
It provides functions for managing expenses and budget operations.

The module implements:
- Expense management (view, add, delete, analyze)
- Budget management (set, view)
- Input validation for all operations

All functions include error handling and input validation to ensure data integrity.
"""

#$fe
## Expenses --------------------------------------------------------------------------------------------------------------------------
def view_expenses(expenses):
    """
    Display all expenses with their details.
    
    This function formats and displays a table of all expenses, including:
    - Index number for reference
    - Date of the expense
    - Category of the expense
    - Description of the expense
    - Amount spent
    It also calculates and displays the total amount spent.
    
    Args:
        expenses (list): List of Expense objects
    """
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    print("\n--- Expenses Summary ---")
    print("Index | Date       | Category    | Description                | Amount")
    print("-" * 75)
    
    total = 0
    for i, expense in enumerate(expenses):
        # Convert amount to float if it's a string
        amount = float(expense.amount) if isinstance(expense.amount, str) else expense.amount
        print(f"{i:<6}| {expense.date} | {expense.category:<10}  | {expense.description:<25}  | ${amount:.2f}")
        total += amount
    
    print("-" * 75)
    print(f"Total Expenses: ${total:.2f}")

def add_new_expense(date_str, amount, category, description):
    """
    Create a new Expense object with the given details.
    
    This function creates a new Expense object using the provided parameters.
    If no date is provided, it uses the current date.
    
    Args:
        date_str (str): Date of the expense in YYYY-MM-DD format
        amount (float): Amount of the expense
        category (str): Category of the expense
        description (str): Detailed description of the expense
        
    Returns:
        Expense: The created Expense object
    """
    # Use today's date if none provided
    if not date_str:
        date_str = datetime.now().strftime("%Y-%m-%d")
    
    return Expense(date_str, amount, category, description)

def delete_expense(expenses, index):
    """
    Delete an expense at the specified index.
    
    This function removes an expense from the list at the given index.
    It includes a safety check to ensure the index is valid.
    
    Args:
        expenses (list): List of Expense objects
        index (int): Index of the expense to delete
    """
    if 0 <= index < len(expenses):
        expenses.pop(index)

def handle_add_expense(expenses):
    """
    Handle the process of adding a new expense with validation.
    
    This function:
    1. Prompts the user for expense details (date, amount, category, description)
    2. Validates each input using appropriate validation functions
    3. Creates a new expense and adds it to the list
    4. Saves the updated expenses list
    
    The function includes error handling and validation loops to ensure
    all inputs are valid before proceeding.
    
    Args:
        expenses (list): List of Expense objects to add to
    """
    print("\n--- Add New Expense ---")
    
    # Get and validate date
    while True:
        date_str = input("Enter date (YYYY-MM-DD) or leave empty for today: ")
        if validate_date(date_str):
            break
        print("Invalid date format. Please use YYYY-MM-DD format.")
    
    # Get and validate amount
    while True:
        try:
            amount_str = input("Enter amount: $")
            amount = validate_amount(amount_str)
            break
        except ValueError as e:
            print(f"Error: {e}")
    
    # Get and validate category
    while True:
        try:
            category = input("Enter expense category (e.g., food, transport, bills): ")
            if not category.strip():
                raise ValueError("Category cannot be empty")
            break
        except ValueError as e:
            print(f"Error: {e}")
    
    # Get and validate description
    while True:
        try:
            description = input("Enter expense description: ")
            if not description.strip():
                raise ValueError("Description cannot be empty")
            break
        except ValueError as e:
            print(f"Error: {e}")
    
    # Add the expense
    expense = add_new_expense(date_str, amount, category, description)
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")

def analyze_expenses(expenses, budget):
    """
    Analyze expenses and provide insights including category-specific analysis.
    """
    if not expenses:
        print("No expenses to analyze.")
        return
    
    # Calculate total expenses
    total = sum(expense.amount for expense in expenses)
    
    # Group expenses by category
    expenses_by_category = {}
    for expense in expenses:
        if expense.category in expenses_by_category:
            expenses_by_category[expense.category] += expense.amount
        else:
            expenses_by_category[expense.category] = expense.amount
    
    print("\n--- Expense Analysis ---")
    print(f"Total expenses: ${total:.2f}")
    print(f"Number of expenses: {len(expenses)}")
    print(f"Average expense: ${total/len(expenses):.2f}")
    
    # Category analysis
    print("\nExpenses by Category:")
    print("Category          | Spent        | Budget        | Remaining")
    print("-" * 65)
    
    for category, spent in expenses_by_category.items():
        category_budget = budget.get_category_budget(category) if budget else 0
        remaining = category_budget - spent if category_budget > 0 else 0
        print(f"{category:<15} | ${spent:>10.2f} | ${category_budget:>10.2f} | ${remaining:>10.2f}")
    
    # Overall budget analysis
    if budget and isinstance(budget, Budget):
        remaining = budget.amount - total
        percentage = (total / budget.amount) * 100
        
        print("\nOverall Budget Status:")
        print(f"Budget remaining: ${remaining:.2f}")
        print(f"Budget usage: {percentage:.1f}%")
        
        if remaining < 0:
            print("Warning: You have exceeded your overall budget!")
        elif percentage > 80:
            print("Warning: You have used more than 80% of your overall budget!")

##-------------------------------------------------------------------------------------------------------------------------------------

## Budget -----------------------------------------------------------------------------------------------------------------------------
def view_budget(budget):
    """
    Display the current budget status.
    
    This function displays the current monthly budget amount.
    If no budget has been set, it informs the user.
    
    Args:
        budget (Budget): The Budget object
    """
    if not budget or not isinstance(budget, Budget):
        print("No budget has been set.")
        return
    
    print("\n--- Budget Status ---")
    print(f"Overall monthly budget: ${budget.amount:.2f}")
    
    if budget.categories:
        print("\nCategory Budgets:")
        print("Category          | Budget Amount")
        print("-" * 35)
        for category, amount in budget.categories.items():
            print(f"{category:<15} | ${amount:.2f}")
        
        total_categories = budget.get_total_category_budgets()
        print("-" * 35)
        print(f"Total category budgets: ${total_categories:.2f}")
        print(f"Remaining for other categories: ${budget.amount - total_categories:.2f}")

def set_budget():
    """
    Set a monthly budget with validation.
    
    This function:
    1. Prompts the user for a monthly budget amount
    2. Validates the input using the validate_budget_amount function
    3. Creates and returns a Budget object
    
    The function includes error handling and allows the user to cancel
    the operation by typing 'cancel'.
    
    Returns:
        Budget: The created Budget object or None if cancelled
    """
    print("\n--- Set Monthly Budget ---")
    
    while True:
        try:
            amount_str = input("Enter monthly budget amount (or 'cancel' to cancel): $")
            if amount_str.lower() == 'cancel':
                return None
            
            amount = validate_budget_amount(amount_str)
            return Budget(amount)
        except ValueError as e:
            print(f"Error: {e}")

def remove_budget(budget):
    """
    Remove the current budget setting.
    
    This function is a placeholder for future implementation.
    """
    pass

## -------------------------------------------------------------------------------------------------------------------------------------