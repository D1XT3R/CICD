import unittest
from app import *

class TestApp(unittest.TestCase):
    def test_run(self):
        self.assertTrue(True)  # простой тест для примера

if __name__ == "__main__":
    unittest.main()
