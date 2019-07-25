from utils.helper import match_percentage
from pwdrequirements.ValidatePassword import validate_password_requirements


def change_password(old_password, new_password):

    if old_password != 'HomeAssignment12345$':
        return False

    if not validate_password_requirements(new_password):
        return False

    if match_percentage(old_password, new_password) >= 80:
        return False

    return True
