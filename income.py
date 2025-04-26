from datetime import datetime
from validation import validate_amount, validate_date

class Income:
    def __init__(self, date, amount, category, description):
        """
        Initialize an Income object.
        
        Args:
            date (str): The date of the income
            amount (float): The amount of the income
            category (str): The category of the income (e.g., salary, freelance, investment)
            description (str): A detailed description of the income
        """
        self.date = date
        self.amount = float(amount)  # Ensure amount is float
        self.category = category
        self.description = description

    @classmethod
    def from_user_input(cls):
        """
        Creates an Income object through interactive user input with error handling.
        
        Returns:
            Income: A new Income object with user-provided values
            None: If the user cancels the operation
            
        Example:
            >>> income = Income.from_user_input()
            Enter date (YYYY-MM-DD) or press enter for today: 2024-03-20
            Enter Amount of the Income: 2500.00
            Enter the category (e.g., salary, freelance, investment): salary
            Enter a description of the income: Monthly salary from employer
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
                        amount_str = input("Enter Amount of the Income: ")
                        amount = validate_amount(amount_str)
                        break  # Exit the amount input loop if successful
                    except ValueError as e:
                        print(f"Error: {str(e)}")
                
                # Category input
                category = input("Enter the category (e.g., salary, freelance, investment): ")
                if not category:
                    raise ValueError("Category cannot be empty")
                
                # Description input
                description = input("Enter a description of the income: ")
                if not description:
                    raise ValueError("Description cannot be empty")
                
                # Create and return the new income object
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
        Creates an Income object from dictionary data.
        
        Args:
            data (dict): Dictionary containing income data
            
        Returns:
            Income: A new Income object
        """
        return cls(
            date=data["date"],
            amount=data["amount"],
            category=data["category"],
            description=data["description"]
        )
    
    def to_dict(self):
        """
        Convert the income to a dictionary for storage.
        
        Returns:
            dict: Dictionary representation of the income
        """
        return {
            "date": self.date,
            "amount": self.amount,
            "category": self.category,
            "description": self.description
        } 