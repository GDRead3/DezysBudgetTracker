from datetime import datetime

class Expense:
    def __init__(self, date, amount, category):
        #constructor for new expenses
        self.date = date            #when the expense occurs
        self.amount = amount        #how much the expense is
        self.category = category    #What category the expense is apart of
    
    

    @classmethod
        #this method provides a way for expenses to be create through user input
    def from_user_input(cls):
            
        #get the date - either the user enters a date or presses enter for today's date
        date = input("Enter date (YYYY-MM-DD) or press enter for today: ")
        if not date:
            #if no date is provided (the user presses enter)

            # datetime.now() gets current date/time
            # strftime converts it to a string in YYYY-MM-DD format
            date = datetime.now().strftime("%Y-%m-%d")
            

        #get the amount of the expense - Error handling to be added later
        amount = float(input("Enter Amount of the Expense: "))

        #Get the Spending category
        category = input("Enter the category (ie. food, transport, bills, etc): ")

        #create and return the new expense object
        return cls(date, amount, category)
        
    #convert the expense into a Dictionary for database
    def to_dict(self):
        return {
            "date": self.date,
            "amount": self.amount,
            "category": self.category
        }

#ensure date is a valid input
def validate_date(date_str):
    try:
        if date_str:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
    except ValueError:
        return False
    return True  # Empty string is valid (will use today's date)

#ensure amount is a valid input
def validate_amount(amount_str):
    try:
        amount = float(amount_str)
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        return amount
    except ValueError as e:
        if str(e) == "Amount must be greater than 0":
            raise
        raise ValueError("Please enter a valid number")

#test:
# Example usage:
#expense_test = expense("2025-02-08", 25.50, "food")
#print(expense_test.amount)  # Prints: 25.50
#print(expense_test.category)  # Prints: food
