import unittest

from ..math_operations import addition_operation, subtraction_operation

class TestMath(unittest.TestCase):
    def test_addition(self):
        addition_result = addition_operation(n1=8, n2=12)
        self.assertEqual(addition_result, 20)

    def test_subtraction(self):
        subtraction_result = subtraction_operation(n1=20, n2=12)
        self.assertEqual(subtraction_result, 8)

if __name__ == '__main__':
    unittest.main()