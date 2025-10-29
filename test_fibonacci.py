"""
Unit tests for the Fibonacci number generator.
"""

import unittest
from fibonacci import fibonacci


class TestFibonacci(unittest.TestCase):
    """Test cases for the fibonacci function."""
    
    def test_fibonacci_base_cases(self):
        """Test base cases F(0) and F(1)."""
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
    
    def test_fibonacci_small_numbers(self):
        """Test small Fibonacci numbers."""
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(8), 21)
        self.assertEqual(fibonacci(9), 34)
        self.assertEqual(fibonacci(10), 55)
    
    def test_fibonacci_larger_numbers(self):
        """Test larger Fibonacci numbers."""
        self.assertEqual(fibonacci(15), 610)
        self.assertEqual(fibonacci(20), 6765)
    
    def test_fibonacci_negative_raises_error(self):
        """Test that negative input raises ValueError."""
        with self.assertRaises(ValueError):
            fibonacci(-1)
        with self.assertRaises(ValueError):
            fibonacci(-10)
    
    def test_fibonacci_non_integer_raises_error(self):
        """Test that non-integer input raises TypeError."""
        with self.assertRaises(TypeError):
            fibonacci(3.5)
        with self.assertRaises(TypeError):
            fibonacci("5")
        with self.assertRaises(TypeError):
            fibonacci(None)
        with self.assertRaises(TypeError):
            fibonacci(True)
        with self.assertRaises(TypeError):
            fibonacci(False)


if __name__ == "__main__":
    unittest.main()
