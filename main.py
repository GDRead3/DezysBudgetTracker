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
            expenses.append(expense)
            print("Expense added successfully!")
        
        elif choice == "2":
            view_expenses(expenses)
        
        elif choice == "3":
            print("Thank you for using the Expense Tracker!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()