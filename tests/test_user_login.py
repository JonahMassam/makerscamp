from seleniumbase  import BaseCase
from faker import Faker
from tests.web_helper import register, login

fake = Faker()

class TestLogin(BaseCase):
    """Testing for login functions"""

    def test_user_login(self):
        """Provided correct details, check a user can login"""

        username = fake.name()
        password = fake.password()

        register(username, password, self)

        # explicit testing despite web helper?
        self.open("http://127.0.0.1:5000/auth/login")
        self.type('input[name="username"]', username)
        self.type('input[name="password"]', password)
        self.click('input[value="Log In"]')

        self.assert_text("Channels")

    def test_user_login_with_wh(self):
        """Provided correct details, test web_helper login function"""

        username = fake.name()
        password = fake.password()

        register(username, password, self)
        login(username, password, self)

        self.assert_text("Channels")

