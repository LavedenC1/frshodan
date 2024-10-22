import unittest
from frshodan.frshodan import frshodan

class Testfrshodan(unittest.TestCase):
    def test_frshodan(self):
        result = frshodan("test_query", 0)
        self.assertIsInstance(result, list)

if __name__ == '__main__':
    unittest.main()
