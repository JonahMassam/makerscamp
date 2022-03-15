from makerscamp.classes import db

class TestDBClass(BaseCase):
  def test_can_instance_class():
    new_db = DB
    assert new_db.test == "hi"