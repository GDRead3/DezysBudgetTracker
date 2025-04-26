from datetime import datetime
from expense import Expense
from budget import Budget
from income import Income
from storage import save_expenses, save_incomes
from validation import validate_date, validate_amount, validate_description, validate_budget_amount, validate_index

"""
Dezy's Budget Tracker - Operations Module

This module contains the core functionality for the budget tracking application.
It provides functions for managing expenses, income, and budget operations.

The module implements:
- Expense management (view, add, delete, analyze)
- Income management (view, add, delete)
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
    if budget and isinstance(budget, Budget) and budget.amount > 0:
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
    if not budget or not isinstance(budget, Budget):
        print("No budget has been set.")
        return
    
    print(f"\nCurrent monthly budget: ${budget.amount:.2f}")
    
    # Add display of category budgets for future use
    if budget.categories:
        print("\nCategory Budgets:")
        for category, amount in budget.categories.items():
            print(f"{category}: ${amount:.2f}")

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

## Income --------------------------------------------------------------------------------------------------------------------------
def view_incomes(incomes):
    """
    Display all incomes with their details.
    
    This function formats and displays a table of all incomes, including:
    - Index number for reference
    - Date of the income
    - Category of the income
    - Description of the income
    - Amount received
    It also calculates and displays the total amount received.
    
    Args:
        incomes (list): List of Income objects
    """
    if not incomes:
        print("No incomes recorded yet.")
        return
    
    print("\n--- Income Summary ---")
    print("Index | Date       | Category    | Description                | Amount")
    print("-" * 75)
    
    total = 0
    for i, income in enumerate(incomes):
        # Convert amount to float if it's a string
        amount = float(income.amount) if isinstance(income.amount, str) else income.amount
        print(f"{i:<6}| {income.date} | {income.category:<10}  | {income.description:<25}  | ${amount:.2f}")
        total += amount
    
    print("-" * 75)
    print(f"Total Income: ${total:.2f}")

def add_new_income(date_str, amount, category, description):
    """
    Create a new income entry.
    
    Args:
        date_str (str): Date of the income in YYYY-MM-DD format
        amount (float): Amount of the income
        category (str): Category of the income
        description (str): Description of the income
        
    Returns:
        Income: A new Income object
    """
    return Income(date_str, amount, category, description)

def delete_income(incomes, index):
    """
    Delete an income entry by index.
    
    Args:
        incomes (list): List of Income objects
        index (int): Index of the income to delete
    """
    if 0 <= index < len(incomes):
        del incomes[index]
    else:
        raise ValueError("Invalid income index")

def handle_add_income(incomes):
    """
    Handle the process of adding a new income entry.
    
    This function:
    1. Prompts the user for income details
    2. Validates the input
    3. Creates a new Income object
    4. Adds it to the list of incomes
    5. Saves the updated list to storage
    
    Args:
        incomes (list): List of Income objects
    """
    print("\n--- Add New Income ---")
    
    # Create a new income object through user input
    new_income = Income.from_user_input()
    
    if new_income:
        # Add the new income to the list
        incomes.append(new_income)
        
        # Save the updated list
        save_incomes(incomes)
        
        print(f"Income of ${new_income.amount:.2f} added successfully!")
    else:
        print("Income addition cancelled.")

def analyze_finances(incomes, expenses, budget):
    """
    Analyze finances by comparing income, expenses, and budget.
    
    This function:
    1. Calculates total income
    2. Calculates total expenses
    3. Calculates net income (income - expenses)
    4. Compares expenses to budget
    5. Provides financial insights
    
    Args:
        incomes (list): List of Income objects
        expenses (list): List of Expense objects
        budget (Budget): Budget object
    """
    if not incomes and not expenses:
        print("No financial data to analyze.")
        return
    
    # Calculate totals
    total_income = sum(float(income.amount) for income in incomes)
    total_expenses = sum(float(expense.amount) for expense in expenses)
    net_income = total_income - total_expenses
    
    # Display financial summary
    print("\n--- Financial Summary ---")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Net Income: ${net_income:.2f}")
    
    # Compare to budget if available
    if budget:
        print(f"Monthly Budget: ${budget.amount:.2f}")
        remaining_budget = budget.amount - total_expenses
        
        if remaining_budget >= 0:
            print(f"Remaining Budget: ${remaining_budget:.2f}")
        else:
            print(f"Budget Exceeded by: ${abs(remaining_budget):.2f}")
        
        # Calculate percentage of budget used
        if budget.amount > 0:
            percentage_used = (total_expenses / budget.amount) * 100
            print(f"Percentage of Budget Used: {percentage_used:.1f}%")
    
    # Provide financial insights
    print("\n--- Financial Insights ---")
    
    if net_income > 0:
        print("You have a positive net income. Good job!")
    elif net_income < 0:
        print("You have a negative net income. Consider reducing expenses or increasing income.")
    else:
        print("Your income equals your expenses. Consider saving more.")
    
    if budget and total_expenses > budget.amount:
        print("You've exceeded your budget. Consider reducing expenses.")
    
    # Analyze income categories
    if incomes:
        print("\n--- Income by Category ---")
        income_by_category = {}
        for income in incomes:
            category = income.category
            amount = float(income.amount)
            if category in income_by_category:
                income_by_category[category] += amount
            else:
                income_by_category[category] = amount
        
        for category, amount in income_by_category.items():
            percentage = (amount / total_income) * 100
            print(f"{category}: ${amount:.2f} ({percentage:.1f}%)")
    
    # Analyze expense categories
    if expenses:
        print("\n--- Expenses by Category ---")
        expenses_by_category = {}
        for expense in expenses:
            category = expense.category
            amount = float(expense.amount)
            if category in expenses_by_category:
                expenses_by_category[category] += amount
            else:
                expenses_by_category[category] = amount
        
        for category, amount in expenses_by_category.items():
            percentage = (amount / total_expenses) * 100
            print(f"{category}: ${amount:.2f} ({percentage:.1f}%)")