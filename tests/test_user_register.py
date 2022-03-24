from seleniumbase import BaseCase
from faker import Faker

fake = Faker()

class TestRegister(BaseCase):
    """Testing for registration functions"""

    def test_register_user(self):
        """Provided correct input, check a new user account can register"""

        # leaving below as is despite tests.web_helper
        # more explicit for future debugging
        self.open("http://127.0.0.1:5000/auth/register")
        username = fake.name()
        password = fake.password()
        self.type('input[name="username"]', username)
        self.type('input[name="password"]', password)
        self.type('input[name="password_confirmation"]', password)
        self.click('input[value="Register"]')

        self.assert_text('Log In')

    def test_register_passwords_match(self):
        """Provided mismatching passwords, check an error message appears"""

        self.open("http://127.0.0.1:5000/auth/register")
        username = fake.name()
        password = fake.password()
        not_password = fake.password()
        self.type('input[name="username"]', username)
        self.type('input[name="password"]', password)
        self.type('input[name="password_confirmation"]', not_password)
        self.click('input[value="Register"]')

        self.assert_text('Both passwords do not match!')
