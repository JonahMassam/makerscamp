def register(username, password, test):
    """Register a user"""
    test.open("http://127.0.0.1:5000/auth/register")
    test.type('input[name="username"]', username)
    test.type('input[name="password"]', password)
    test.type('input[name="password_confirmation"]', password)
    test.click('input[value="Register"]')

def login(username, password, test):
    """Login a user"""
    test.open("http://127.0.0.1:5000/auth/login")
    test.type('input[name="username"]', username)
    test.type('input[name="password"]', password)
    test.click('input[value="Log In"]')
