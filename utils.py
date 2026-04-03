"""Utilities module for helper functions and utilities"""

def format_currency(amount):
    """Format amount as currency"""
    return f"₹{amount:,.2f}"

def format_date(date_string):
    """Format date string"""
    return date_string

def validate_email(email):
    """Validate email format"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    """Validate phone number"""
    import re
    pattern = r'^[0-9]{10}$'
    return re.match(pattern, phone) is not None
