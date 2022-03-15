from makerscamp.db import *

class TestDBClass:
  def test_can_instance_class(self):
    new_db = DB
    assert new_db.test() == "hi"