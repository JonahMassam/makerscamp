from seleniumbase import BaseCase
from faker import Faker

fake = Faker()

class TestRegister(BaseCase):
    def test_register_user(self):
        self.open("http://127.0.0.1:5000/auth/register")
        username = fake.name()
        password = fake.password()
        self.type('input[name="username"]', username)
        self.type('input[name="password"]', password)
        self.type('input[name="password_confirmation"]', password)
        self.click('input[value="Register"]')

        self.assert_text('Log In')

    def test_register_passwords_match(self):
        self.open("http://127.0.0.1:5000/auth/register")
        username = fake.name()
        password = fake.password()
        not_password = fake.password()
        self.type('input[name="username"]', username)
        self.type('input[name="password"]', password)
        self.type('input[name="password_confirmation"]', not_password)
        self.click('input[value="Register"]')

        self.assert_text('Both passwords do not match!')
