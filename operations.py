from datetime import datetime
from models import Expense, Budget
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

## Expenses --------------------------------------------------------------------------------------------------------------------------
def view_expenses(expenses):
    """
    Display all expenses with their details.
    
    This function formats and displays a table of all expenses, including:
    - Index number for reference
    - Date of the expense
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
    print("Index | Date       | Description                | Amount")
    print("-" * 60)
    
    total = 0
    for i, expense in enumerate(expenses):
        print(f"{i:<6}| {expense.date} | {expense.description:<25} | ${expense.amount:.2f}")
        total += expense.amount
    
    print("-" * 60)
    print(f"Total Expenses: ${total:.2f}")

def add_new_expense(date_str, description, amount):
    """
    Create a new Expense object with the given details.
    
    This function creates a new Expense object using the provided parameters.
    If no date is provided, it uses the current date.
    
    Args:
        date_str (str): Date of the expense in YYYY-MM-DD format
        description (str): Description of the expense
        amount (float): Amount of the expense
        
    Returns:
        Expense: The created Expense object
    """
    # Use today's date if none provided
    if not date_str:
        date_str = datetime.now().strftime("%Y-%m-%d")
    
    return Expense(date_str, description, amount)

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
    1. Prompts the user for expense details (date, description, amount)
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
    
    # Get and validate description
    while True:
        try:
            description = input("Enter expense description: ")
            description = validate_description(description)
            break
        except ValueError as e:
            print(f"Error: {e}")
    
    # Get and validate amount
    while True:
        try:
            amount_str = input("Enter amount: $")
            amount = validate_amount(amount_str)
            break
        except ValueError as e:
            print(f"Error: {e}")
    
    # Add the expense
    expense = add_new_expense(date_str, description, amount)
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")

def analyze_expenses(expenses, budget):
    """
    Analyze expenses and provide insights.
    
    This function analyzes the expense data and provides useful insights:
    1. Total amount spent
    2. Number of expenses recorded
    3. Average expense amount
    4. Date with the highest expenses
    5. Budget comparison (if a budget is set)
    
    The function includes warnings for budget overruns or high usage.
    
    Args:
        expenses (list): List of Expense objects
        budget (Budget): The Budget object
    """
    if not expenses:
        print("No expenses to analyze.")
        return
    
    # Calculate total expenses
    total = sum(expense.amount for expense in expenses)
    
    # Group expenses by date
    expenses_by_date = {}
    for expense in expenses:
        if expense.date in expenses_by_date:
            expenses_by_date[expense.date] += expense.amount
        else:
            expenses_by_date[expense.date] = expense.amount
    
    # Find date with highest expenses
    highest_date = max(expenses_by_date, key=expenses_by_date.get)
    highest_amount = expenses_by_date[highest_date]
    
    # Calculate average expense
    average = total / len(expenses)
    
    print("\n--- Expense Analysis ---")
    print(f"Total expenses: ${total:.2f}")
    print(f"Number of expenses: {len(expenses)}")
    print(f"Average expense: ${average:.2f}")
    print(f"Date with highest expenses: {highest_date} (${highest_amount:.2f})")
    
    # Budget comparison
    if budget and budget.amount > 0:
        remaining = budget.amount - total
        percentage = (total / budget.amount) * 100
        
        print(f"\nBudget status: ${remaining:.2f} remaining")
        print(f"Budget usage: {percentage:.1f}%")
        
        if remaining < 0:
            print("Warning: You have exceeded your budget!")
        elif percentage > 80:
            print("Warning: You have used more than 80% of your budget!")

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
    if not budget or budget.amount <= 0:
        print("No budget has been set.")
        return
    
    print(f"\nCurrent monthly budget: ${budget.amount:.2f}")

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