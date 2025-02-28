from datetime import datetime

#ensure date is a valid input
def validate_date(date_str):
    """
    Validates if the input string is a valid date in YYYY-MM-DD format.
    
    Args:
        date_str (str): The date string to validate
        
    Returns:
        bool: True if date is valid or empty, False otherwise
        
    Example:
        >>> validate_date("2024-03-15")
        True
        >>> validate_date("invalid")
        False
    """
    try:
        if date_str:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
    except ValueError:
        return False
    return True  # Empty string is valid (will use today's date)

#ensure amount is a valid input
def validate_amount(amount_str):
    """
    Validates and converts string amount to float. Amount must be positive.
    
    Args:
        amount_str (str): The amount string to validate
        
    Returns:
        float: The validated amount as a float
        
    Raises:
        ValueError: If amount is not a valid positive number
        
    Example:
        >>> validate_amount("50.25")
        50.25
        >>> validate_amount("-10")
        ValueError: Amount must be greater than 0
    """
    try:
        amount = float(amount_str)
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        return amount
    except ValueError as e:
        if str(e) == "Amount must be greater than 0":
            raise
        raise ValueError("Please enter a valid number")

def validate_menu_choice(choice, valid_options):
    """
    Validates if the input choice is within the valid options.
    
    Args:
        choice (str): The user's input choice
        valid_options (list): List of valid options
        
    Returns:
        bool: True if choice is valid, False otherwise
        
    Example:
        >>> validate_menu_choice("1", ["1", "2", "3"])
        True
        >>> validate_menu_choice("4", ["1", "2", "3"])
        False
    """
    return choice in valid_options

def validate_index(index_str, max_index):
    """
    Validates if the input index is within valid range.
    
    Args:
        index_str (str): The index string to validate
        max_index (int): The maximum valid index
        
    Returns:
        int: The validated index as an integer
        
    Raises:
        ValueError: If index is not a valid integer or out of range
        
    Example:
        >>> validate_index("2", 5)
        2
        >>> validate_index("10", 5)
        ValueError: Index out of range
    """
    try:
        index = int(index_str)
        if index < 0 or index >= max_index:
            raise ValueError("Index out of range")
        return index
    except ValueError as e:
        if str(e) == "Index out of range":
            raise
        raise ValueError("Please enter a valid number")

def validate_description(description):
    """
    Validates if the expense description is not empty and within reasonable length.
    
    Args:
        description (str): The description to validate
        
    Returns:
        str: The validated description
        
    Raises:
        ValueError: If description is empty or too long
        
    Example:
        >>> validate_description("Grocery shopping")
        'Grocery shopping'
        >>> validate_description("")
        ValueError: Description cannot be empty
    """
    description = description.strip()
    if not description:
        raise ValueError("Description cannot be empty")
    if len(description) > 100:
        raise ValueError("Description must be less than 100 characters")
    return description

def validate_budget_amount(amount_str):
    """
    Validates and converts budget amount string to float. Budget must be positive.
    
    Args:
        amount_str (str): The budget amount string to validate
        
    Returns:
        float: The validated budget amount as a float
        
    Raises:
        ValueError: If budget amount is not a valid positive number
        
    Example:
        >>> validate_budget_amount("1000")
        1000.0
        >>> validate_budget_amount("0")
        ValueError: Budget amount must be greater than 0
    """
    try:
        amount = float(amount_str)
        if amount <= 0:
            raise ValueError("Budget amount must be greater than 0")
        return amount
    except ValueError as e:
        if str(e) == "Budget amount must be greater than 0":
            raise
        raise ValueError("Please enter a valid budget amount")