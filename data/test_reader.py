from unittest import TestCase
from reader import Reader
from database.data import Data


class TestReader(TestCase):
    def test_commit(self):
        Data().delete_all()
        r = Reader("resource\SMU工商旅游管科电商16.txt")
        r.parse()
        print(r.commit())
