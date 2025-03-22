from datetime import datetime
from validation import validate_amount, validate_date

class Expense:
    def __init__(self, date, amount, category, description):
        """
        Initialize an Expense object.
        
        Args:
            date (str): The date of the expense
            amount (float): The amount of the expense
            category (str): The category of the expense (e.g., food, transport, bills)
            description (str): A detailed description of the expense
        """
        self.date = date
        self.amount = float(amount)  # Ensure amount is float
        self.category = category
        self.description = description

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
            Enter the category (e.g., food, transport, bills): food
            Enter a description of the expense: Lunch at the local cafe
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
                category = input("Enter the category (e.g., food, transport, bills): ").strip()
                if not category:
                    raise ValueError("Category cannot be empty")
                
                # Description input and validation
                description = input("Enter a description of the expense: ").strip()
                if not description:
                    raise ValueError("Description cannot be empty")
                
                # Create and return the new expense object
                return cls(date, amount, category, description)
                
            except ValueError as e:
                print(f"Error: {str(e)}")
                # Allow user to retry or cancel
                retry = input("Would you like to try again? (y/n): ")
                if retry.lower() != 'y':
                    return None
        
    @classmethod
    def from_dict(cls, data):
        """
        Create an Expense object from a dictionary.
        
        Args:
            data (dict): Dictionary containing expense data
            
        Returns:
            Expense: A new Expense object
        """
        return cls(
            date=data['date'],
            amount=data['amount'],
            category=data['category'],
            description=data['description']
        )

    def to_dict(self):
        """
        Convert the expense to a dictionary for JSON storage.
        
        Returns:
            dict: Dictionary representation of the expense
        """
        return {
            "date": self.date,
            "amount": self.amount,
            "category": self.category,
            "description": self.description
        }
    

#test:
# Example usage:
#expense_test = expense("2025-02-08", 25.50, "food", "Lunch at the local cafe")
#print(expense_test.amount)  # Prints: 25.50
#print(expense_test.category)  # Prints: food
#print(expense_test.description)  # Prints: Lunch at the local cafe
