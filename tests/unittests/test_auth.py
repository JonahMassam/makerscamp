from makerscamp.classes.auth import *

class TestAuthClass:
  def test_auth_class_exists(self):
    assert Auth.test() == "test"