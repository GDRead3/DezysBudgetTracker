from operations import view_expenses, add_new_expense, delete_expense, handle_add_expense, set_budget, view_budget, analyze_expenses
from storage import save_expenses, load_expenses, save_budget, load_budget
from validation import validate_menu_choice, validate_index, validate_description, validate_amount, validate_budget_amount

"""
Dezy's Budget Tracker - Main Module

This module serves as the entry point for the budget tracking application.
It provides a command-line interface for users to manage their expenses and budget.

The application offers the following features:
- Quick expense addition
- Expense management (view, add, delete)
- Budget management (set, view, analyze)

All user inputs are validated to ensure data integrity and prevent errors.
"""

def main():
    """
    Main function that runs the budget tracker application.
    
    This function:
    1. Loads existing expenses and budget data
    2. Displays the main menu
    3. Handles user input with validation
    4. Routes to appropriate functionality based on user choice
    5. Provides error handling for invalid inputs
    
    The application continues running until the user chooses to exit.
    """
    expenses = load_expenses()
    budget = load_budget()
    while True:
        print("\n1. Quick Add Expense")
        print("2. Expenses Management")
        print("3. Budget Management")
        print("4. Exit")
        
        choice = input("\nChoose an option (1-4): ")
        
        # Validate menu choice
        if not validate_menu_choice(choice, ["1", "2", "3", "4"]):
            print("Invalid choice. Please enter a number between 1 and 4.")
            continue
        
        if choice == "1":
            handle_add_expense(expenses)
        
        elif choice == "2":
            # Expenses Management submenu
            print("\nExpenses Management")
            print("1. View Expenses Summary")
            print("2. Add Expense")
            print("3. Delete Expense")
            print("4. Back to Main Menu")
            sub_choice = input("\nChoose an option (1-4): ")
            
            # Validate submenu choice
            if not validate_menu_choice(sub_choice, ["1", "2", "3", "4"]):
                print("Invalid choice. Please enter a number between 1 and 4.")
                continue
            
            if sub_choice == "1":
                view_expenses(expenses)
            elif sub_choice == "2":
                handle_add_expense(expenses)
            elif sub_choice == "3":
                # Check if there are expenses to delete
                if not expenses:
                    print("No expenses to delete.")
                    continue
                
                view_expenses(expenses)
                try:
                    # Get and validate expense index
                    expense_index_str = input("Enter the index of the expense to delete: ")
                    expense_index = validate_index(expense_index_str, len(expenses))
                    delete_expense(expenses, expense_index)
                    save_expenses(expenses)
                    print("Expense deleted successfully!")
                except ValueError as e:
                    print(f"Error: {e}")
            elif sub_choice == "4":
                continue

        elif choice == "3":
            # Budget Management submenu
            print("\nBudget Management")
            print("1. Set Monthly Budget")
            print("2. View Budget Status")
            print("3. Analyze Expenses")
            print("4. Back to Main Menu")
            sub_choice = input("\nChoose an option (1-4): ")

            # Validate submenu choice
            if not validate_menu_choice(sub_choice, ["1", "2", "3", "4"]):
                print("Invalid choice. Please enter a number between 1 and 4.")
                continue

            if sub_choice == "1":
                try:
                    # Set budget with validation
                    budget = set_budget()
                    if budget:
                        save_budget(budget.amount)
                        print(f"Monthly budget set to ${budget.amount:.2f}")
                    else:
                        print("Budget setting cancelled.")
                except ValueError as e:
                    print(f"Error: {e}")
            elif sub_choice == "2":
                budget = load_budget()
                view_budget(budget)
            elif sub_choice == "3":
                # Check if there are expenses to analyze
                if not expenses:
                    print("No expenses to analyze.")
                    continue
                analyze_expenses(expenses, budget)
            elif sub_choice == "4":
                continue
        
        elif choice == "4":
            print("Thank you for using the Dezy's Budget Tracker!")
            break

if __name__ == "__main__":
    main()