import unittest
from app.database import engine

class TestDatabase(unittest.TestCase):

    def test_connection(self):
        try:
            conn = engine.connect()
            self.assertIsNotNone(conn)
            conn.close()
        except Exception as e:
            self.fail(f"Database connection failed: {e}")


if __name__ == "__main__":
    unittest.main()