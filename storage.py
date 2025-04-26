import json
from datetime import datetime
from expense import Expense
from budget import Budget
from income import Income

#saving a list of expense objects to a JSON file
def save_expenses(expenses, filename="expenses.json"):
    #uses the "to_dict" function from the Expense class to convert the data into a list for the JSON file
    expense_data = [expense.to_dict() for expense in expenses]

    #write the JSON file

    with open(filename, "w") as f: # "w" means write
        json.dump(expense_data, f, indent=4)

def load_expenses(filename="expenses.json"):
    try:
        with open(filename, "r") as f: # "r" means read
            expenses_data = json.load(f)

        #Convert Dictionary back into Expense object
        expenses = []
        for expense_dict in expenses_data:
            expense = Expense(
                date = expense_dict["date"],
                amount = expense_dict["amount"],
                category = expense_dict["category"],
                description = expense_dict["description"]
            )
            expenses.append(expense)
        
        return expenses
    
    except FileNotFoundError:
        #if there is no file, the fuction will return an empty list
        return []
    

## Budgets--------------------------------------------------------------------------------------------------------

def save_budget(budget, filename="budget.json"):
    """
    Save budget object to JSON file.
    """
    if isinstance(budget, Budget):
        budget_data = budget.to_dict()
    else:
        budget_data = {"amount": float(budget), "categories": {}}
        
    with open(filename, "w") as f:
        json.dump(budget_data, f, indent=4)

def load_budget(filename="budget.json"):
    """
    Load budget from JSON file.
    """
    try:
        with open(filename, "r") as f:
            budget_data = json.load(f)
        return Budget.from_dict(budget_data)
    except FileNotFoundError:
        return None

## Income--------------------------------------------------------------------------------------------------------

def save_incomes(incomes, filename="incomes.json"):
    """
    Save a list of income objects to a JSON file.
    
    Args:
        incomes (list): List of Income objects
        filename (str): Name of the file to save to
    """
    income_data = [income.to_dict() for income in incomes]
    
    with open(filename, "w") as f:
        json.dump(income_data, f, indent=4)

def load_incomes(filename="incomes.json"):
    """
    Load incomes from JSON file.
    
    Args:
        filename (str): Name of the file to load from
        
    Returns:
        list: List of Income objects
    """
    try:
        with open(filename, "r") as f:
            incomes_data = json.load(f)
            
        incomes = []
        for income_dict in incomes_data:
            income = Income(
                date=income_dict["date"],
                amount=income_dict["amount"],
                category=income_dict["category"],
                description=income_dict["description"]
            )
            incomes.append(income)
        
        return incomes
    
    except FileNotFoundError:
        # If there is no file, the function will return an empty list
        return []