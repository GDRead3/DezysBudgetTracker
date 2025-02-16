from datetime import datetime

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
    """Validates and converts string amount to float"""
    try:
        amount = float(amount_str)
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        return amount
    except ValueError:
        raise ValueError("Please enter a valid number")