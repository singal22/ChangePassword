import pytest
from pwdrequirements.ValidatePassword import validate_password_requirements
from pwdrequirements.ChangePassword import change_password


class TestPassword:

    """
    Test Password
    """

    @pytest.mark.parametrize("test_case,user_input,output", [
        ('Test valid password', 'Himanshu123456789&@', True),
        ('Test not allowed special characters', '()()', False),
        ('Test total characters < 18 ', 'Himanshu', False),
        ('Test allowed characters but less than 18', 'Himanshu123@', False),
        ('Test only lowercase letters = 18', 'himanshuhimanshuhi', False),
        ('Test only uppercase letters = 18', 'HIMANSHUHIMANSHUHI', False),
        ('Test only numbers = 18', '123456789123456789', False),
        ('Test only allowed special = 18', '!@#$&*!@#$&*!@#$&*', False),
        ('Test only lower and upper letters > 18', 'HimanshuHimanshuHim', False),
        ('Test requirement except upper case letters', 'himanshu123456789&@', False),
        ('Test requirement except lower case letters', 'HIMANSHHU123456789&@', False),
        ('Test valid with max 4 special', 'Himanshu123456789#$&*', True),
        ('Test password having number > 50%', 'Himanshu123456789!123456789123456789', False),
        ('Test password having number = 50%', 'Himanshu!@#$123456789123', False),
        ('Test duplicate characters more than 4', 'HIMANSHHU123456789&@HH', False),
        ('Test empty', '', False),
        ('Test spaces', '   ', False),
        ('Test words', 'Himanshu 123456 $@$@   ', False),
        ('Test more than 4 special characters','Himanshu123456789&$&$$', False)
    ])
    def test_validate_requirements_pwd(self, test_case, user_input, output):
        """
        The actual test.
        Any method which starts with ``test_`` will considered as a test case.
        """

        assert validate_password_requirements(user_input) == output,\
            ' Validation pwdrequirements failed:' + test_case + ':' + user_input

    @pytest.mark.parametrize("test_case,old_pwd,new_pwd, output", [
        ('Test valid old password and new password', 'HomeAssignment123$', 'Himanshu123456789&@', True),
        ('Test invalid old password with valid new', 'Home', 'Himanshu123456789&@', False),
        ('Test invalid old password and invalid new', 'Home', 'Hi', False),
    ])
    def test_old_pwd_requirements(self, test_case, old_pwd, new_pwd, output):
        """
        Test old password with System
        """

        assert change_password(old_pwd, new_pwd) == output,\
            ' Validation old password failed:' + test_case + ':' + old_pwd