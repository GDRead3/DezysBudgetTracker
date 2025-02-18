from operations import view_expenses, add_new_expense, delete_expense, handle_add_expense, set_budget, view_budget
from storage import save_expenses, load_expenses, save_budget, load_budget




def main():
    expenses = load_expenses()
    budget = load_budget()
    while True:
        print("\n1. Quick Add Expense")
        print("2. Expenses Management")
        print("3. Budget Management")
        print("4. Exit")
        
        choice = input("\nChoose an option (1-4): ")
        
        if choice == "1":
            handle_add_expense(expenses)
        
        elif choice == "2":
            print("\nExpenses Management")
            print("1. View Expenses Summary")
            print("2. Add Expense")
            print("3. Delete Expense")
            print("4. Back to Main Menu")
            sub_choice = input("\nChoose an option (1-4): ")
            
            if sub_choice == "1":
                view_expenses(expenses)
            elif sub_choice == "2":
                handle_add_expense(expenses)
            elif sub_choice == "3":
                expense_index = int(input("Enter the index of the expense to delete: "))
                delete_expense(expenses, expense_index)
                save_expenses(expenses)
                print("Expense deleted successfully!")
            elif sub_choice == "4":
                continue

        elif choice == "3":
            print("Budget Management")
            print("1. Set Monthly Budget")
            print("2. View Budget Status")
            print("3. Analyze Expenses")
            print("4. Back to Main Menu")
            sub_choice = input("\nChoose an option (1-4): ")

            if sub_choice == "1":
                budget = set_budget()
                if budget:
                    save_budget(budget.amount)
                    print(f"Monthly budget set to ${budget.amount:.2f}")
                else:
                    print("Budget setting cancelled.")
            elif sub_choice == "2":
                budget = load_budget()
                view_budget(budget)
            elif sub_choice == "3":
                pass
            elif sub_choice == "4":
                continue


        
            
        
        elif choice == "4":
            print("Thank you for using the Dezy's Budget Tracker!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()