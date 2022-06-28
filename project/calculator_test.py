import unittest
from project.calculator import Calculator

class Test_sum(unittest.TestCase):
    def test_sum(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(1,2),3)

if __name__ == "__main__":
    unittest.main()
