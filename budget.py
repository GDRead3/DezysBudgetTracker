from validation import validate_amount

class Budget:
    """
    Represents a budget with amount and future extensibility for sub-budgets.
    
    Attributes:
        amount (float): The total budget amount
        categories (dict): Dictionary to store category-specific sub-budgets
    """
    def __init__(self, amount):
        self.amount = float(amount)
        self.categories = {}  # Prepare for future category budgets
    
    def to_dict(self):
        """
        Convert the budget to a dictionary for storage.
        """
        return {
            "amount": self.amount,
            "categories": self.categories
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Create a Budget object from dictionary data.
        """
        budget = cls(data["amount"])
        budget.categories = data.get("categories", {})
        return budget

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
                

#Sub Budget-----------------------------------------------------------------------------------------------------------

class SubBudget(Budget):  # Fixed class name to follow Python naming conventions
    def __init__(self, amount, category):
        super().__init__(amount)
        self.category = category