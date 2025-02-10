from operations import view_expenses, add_new_expense

def main():
    expenses = []
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        
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
            view_expenses(expenses)
        
        elif choice == "3":
            print("Thank you for using the Dezy's Budget Tracker!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()