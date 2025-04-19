from validation import validate_amount

class Budget:
    """
    Represents a budget with overall amount and category-specific sub-budgets.
    
    Attributes:
        amount (float): The total budget amount
        categories (dict): Dictionary to store category-specific sub-budgets
    """
    def __init__(self, amount):
        self.amount = float(amount)
        self.categories = {}  # Format: {category: amount}
    
    def set_category_budget(self, category, amount):
        """
        Set a budget for a specific category.
        
        Args:
            category (str): The expense category
            amount (float): The budget amount for this category
        """
        self.categories[category] = float(amount)
    
    def get_category_budget(self, category):
        """
        Get the budget for a specific category.
        
        Args:
            category (str): The expense category
            
        Returns:
            float: The budget amount for the category, or 0 if not set
        """
        return self.categories.get(category, 0)
    
    def get_total_category_budgets(self):
        """
        Calculate the total of all category budgets.
        
        Returns:
            float: Sum of all category budgets
        """
        return sum(self.categories.values())
    
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
                # Get overall budget
                amount_str = input("Enter overall monthly budget amount: $")
                amount = validate_amount(amount_str)
                budget = cls(amount)
                
                # Ask for category budgets
                while True:
                    add_category = input("\nWould you like to set a category budget? (y/n): ").lower()
                    if add_category != 'y':
                        break
                    
                    category = input("Enter category name (e.g., food, transport): ").strip()
                    if not category:
                        print("Category name cannot be empty.")
                        continue
                    
                    amount_str = input(f"Enter budget amount for {category}: $")
                    try:
                        amount = validate_amount(amount_str)
                        budget.set_category_budget(category, amount)
                    except ValueError as e:
                        print(f"Error: {e}")
                        continue
                
                return budget
                
            except ValueError as e:
                print(f"Error: {e}")
                retry = input("Would you like to try again? (y/n): ")
                if retry.lower() != 'y':
                    return None

#Sub Budget-----------------------------------------------------------------------------------------------------------

class SubBudget(Budget):  # Fixed class name to follow Python naming conventions
    def __init__(self, amount, category):
        super().__init__(amount)
        self.category = category