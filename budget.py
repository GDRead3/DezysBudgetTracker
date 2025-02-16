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