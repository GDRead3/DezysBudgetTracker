import json
from datetime import datetime
from expense import Expense

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
                category = expense_dict["category"]
            )
            expenses.append(expense)
        
        return expenses
    
    except FileNotFoundError:
        #if there is no file, the fuction will return an empty list
        return []
    

## --------------------------------------------------------------------------------------------------------

def save_budget(budget, filename="budget.json"):
    with open(filename, "w") as f:
        json.dump({"amount": budget}, f, indent=4)

def load_budget(filename="budget.json"):
    try:
        with open(filename, "r") as f:
            budget_data = json.load(f)
        return budget_data["amount"]
    except FileNotFoundError:
        return None