from operations import view_expenses, add_new_expense, delete_expense

def main():
    expenses = []
    while True:
        print("\n1. Add Expense")
        print("2. Expenses Management")
        print("3. Budget Management")
        print("4. Exit")
        
        choice = input("\nChoose an option (1-3): ")
        
        if choice == "1":
            expense = add_new_expense()
            #if expense is not None, add it to the list
            if expense:
                expenses.append(expense)
                print("Expense added successfully!")
            else:
                print("Expense addition cancelled.")
        
        elif choice == "2":
            print("\nExpenses Management")
            print("1. View Expenses")
            print("2. Delete Expense")
            print("3. Back to Main Menu")
            sub_choice = input("\nChoose an option (1-3): ")

            if sub_choice == "1":
                view_expenses(expenses)
            elif sub_choice == "2":
                expense_index = int(input("Enter the index of the expense to delete: "))
                delete_expense(expenses, expense_index)
                print("Expense deleted successfully!")
            elif sub_choice == "3":
                break

        elif choice == "3":
            print("Budget Management")
            print("1. Set Monthly Budget")
            print("2. View Budget Status")
            print("3. Analyze Expenses")
            print("4. Back to Main Menu")
            
        
        elif choice == "4":
            print("Thank you for using the Dezy's Budget Tracker!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()