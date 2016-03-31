import unittest
from operations.operations import factorial, summation


class TddInPythonExample(unittest.TestCase):

    def test_factorial_operation_returns_correct_result(self):
        result = factorial(2)
        self.assertEqual(2, result)

    def test_summation_operation_returns_correct_result(self):
        result = summation(2)
        self.assertEqual(3, result)
