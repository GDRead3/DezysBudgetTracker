from expense import expense

def view_expenses(expenses):
# check if we have expense to show
    if not expenses:
        print("No expenses to show!")
        return
    
    #header for expenses table
    print ("\nYour Expenses:")
    print ("Date\tAmount\tCategory")
    print ("-" * 40) #creates a line to divide header from results

view_expenses(expense)