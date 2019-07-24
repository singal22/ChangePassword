import re
from utils.helper import (
    count_special_characters,
    count_digits,
    count_duplicate)

# Function to validate the pwd requirements
special_chars = ['@', '#', '$', '&', '!', '*']


def validate_password_requirements(pwd):

    success = True

    if not re.match(r'^[A-Za-z0-9@#$&!*]+$', pwd):
        # Allowed characters
        success = False

    if len(pwd) < 18:
        # length of pwd requirements should be atleast 18
        success = False

    if not any(char.isupper() for char in pwd):
        # Password should have at least one uppercase letter
        success = False

    if not any(char.islower() for char in pwd):
        # Password should have at least one lowercase letter
        success = False

    if not any(char.isdigit() for char in pwd):
        # Password should have at least one numeral
        success = False

    if not any(char in special_chars for char in pwd):
        # Password should have at least one of the special characters !@#$&*
        success = False

    # Password should not have more than 4 special characters
    if count_special_characters(pwd, special_chars) > 4:
        success = False

    # Password should not have more than 50% numbers
    if count_digits(pwd) > (len(pwd)/2):
        success = False

    # No duplicate repeat characters more than 4
    if count_duplicate(pwd, 4):
        success = False

    return success
