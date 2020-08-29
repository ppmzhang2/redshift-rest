import unittest
from datetime import date

from redshift.models.dao import Dao
from redshift.models.tables import Users


class TestModel(unittest.TestCase):
    dao = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.dao = Dao(echo=True)

    @classmethod
    def tearDownClass(cls) -> None:
        del cls.dao

    def setUp(self):
        self.dao.reset_engine()

    def tearDown(self):
        self.dao.reset_engine()

    def test_create_drop(self):
        """test creating & dropping tables

        methods:
          * dao.create_all
          * dao.drop_all
          * dao.all_tables

        """
        exp = {
            'sales', 'listing', 'event', 'users', 'venue', 'category', 'date'
        }
        self.dao.create_all()
        self.dao.drop_all()
        self.dao.create_all()
        tables = self.dao.all_tables()
        self.assertEqual(exp, set(tables))


if __name__ == '__main__':
    unittest.main(verbosity=2)
