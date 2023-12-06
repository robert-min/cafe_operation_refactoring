from libs.db_manager import MySQLManager
from unittest import TestCase

class TestRepository(MySQLManager):
    def __init__(self) -> None:
        super().__init__()

    def session_connect(self) -> str:
        try:
            with self.session:
                return "Success session connect."
        except Exception:
            return "Failed session connect."


class MySQLManagerSessionConnectTest(TestCase):
    def test_session_connect(self):
        repo = TestRepository()
        self.assertEqual(repo.session_connect(), "Success session connect.")
