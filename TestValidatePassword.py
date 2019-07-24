import pytest
from pwdrequirements.ValidatePassword import validate_password_requirements


class TestValidatePassword:

    """
    Test Validate Password
    """

    @pytest.mark.parametrize("input,output", [
        ('Himanshu', False),
        ('Himanshu123', False),
        ('123456789123456789', False),
        ('!@#$&*!@#$&*!@#$&*', False),
        ('HimanshuHimanshuHim', False),
        ('Himanshu12345678&', False),
        ('Himanshu123456789&@', True),
        ('himanshu123456789&@', False),
        ('HIMANSHHU123456789&@', False),
        ('Himanshu123456789!@#', True),
        ('Himanshu123456789#$&*', True),
        ('Himanshu123456789!123456789123456789', False),
        ('Himanshu!@#$123456789123', True),
        ('HIMANSHHU123456789&@HH', False),
        ('', False),
        ('   ', False),
    ])
    def test_validate_requirements_pwd(self, input, output):
        """
        The actual test.
        Any method which starts with ``test_`` will considered as a test case.
        """

        assert validate_password_requirements(input) == output,\
            ' Validation pwdrequirements failed: ' + input
