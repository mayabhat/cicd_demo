import os
import unittest
from math_ops import add, subtract, multiply, remainder

class TestMethods(unittest.TestCase):
    def test_add(self):
        assert add(2, 3) == 5

    def test_subtract(self):
        assert subtract(3, 2) == 1

    def test_multiply(self):
        assert multiply(3, 2) == 6

    def test_remainder(self):
        assert remainder(3, 2) == 1

if __name__ == "__main__":
    unittest.main(warnings="ignore")
