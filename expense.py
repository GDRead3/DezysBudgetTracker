from datetime import datetime

class Expense:
    def __init__(self, date, amount, category):
        #constructor for new expenses
        self.date = date            #when the expense occurs
        self.amount = amount        #how much the expense is
        self.category = category    #What category the expense is apart of
    
    

    @classmethod
    def from_user_input(cls):
        """
        Creates an Expense object through interactive user input with error handling.
        
        Returns:
            Expense: A new Expense object with user-provided values
            None: If the user cancels the operation
            
        Example:
            >>> expense = Expense.from_user_input()
            Enter date (YYYY-MM-DD) or press enter for today: 2024-03-20
            Enter Amount of the Expense: 42.50
            Enter the category (ie. food, transport, bills, etc): food
        """
        while True:
            try:
                # Date input and validation
                date = input("Enter date (YYYY-MM-DD) or press enter for today: ")
                if not validate_date(date):
                    raise ValueError("Invalid date format. Please use YYYY-MM-DD")
                
                # Use current date if no date provided
                if not date:
                    date = datetime.now().strftime("%Y-%m-%d")
                
                # Amount input with retry loop
                while True:
                    try:
                        amount_str = input("Enter Amount of the Expense: ")
                        amount = validate_amount(amount_str)
                        break  # Exit the amount input loop if successful
                    except ValueError as e:
                        print(f"Error: {str(e)}")
                
                # Category input and validation
                category = input("Enter the category (ie. food, transport, bills, etc): ").strip()
                if not category:
                    raise ValueError("Category cannot be empty")
                
                # Create and return the new expense object
                return cls(date, amount, category)
                
            except ValueError as e:
                print(f"Error: {str(e)}")
                # Allow user to retry or cancel
                retry = input("Would you like to try again? (y/n): ")
                if retry.lower() != 'y':
                    return None
        
    #convert the expense into a Dictionary for database
    def to_dict(self):
        return {
            "date": self.date,
            "amount": self.amount,
            "category": self.category
        }
    
class Budget:
    def __init__(self, amount):
        self.amount = amount

    @classmethod
    def from_user_input(cls):
        """
        Creates an Budget object through interactive user input with error handling.
        
        Returns:
            Budget: A new Budget object with user-provided values
            None: If the user cancels the operation
        
        """
        while True:
            try:
                # Amount input with retry loop
                while True:
                    try:
                        amount_str = input("Enter Amount for the Budget: ")
                        amount = validate_amount(amount_str)
                        break  # Exit the amount input loop if successful
                    except ValueError as e:
                        print(f"Error: {str(e)}")
                
                
                # Create and return the new budget object
                return cls(amount)
                
            except ValueError as e:
                print(f"Error: {str(e)}")
                # Allow user to retry or cancel
                retry = input("Would you like to try again? (y/n): ")
                if retry.lower() != 'y':
                    return None

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
