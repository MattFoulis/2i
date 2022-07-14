from iterate import multiples
import unittest

class TestMultiples(unittest.TestCase):
    """Test cases for multiples functions. 
    """

    # Iterate in multiples of A until X
    def test_multiples(self):
        result = multiples.multiples(1, 5)
        self.assertListEqual(result, [1, 2, 3, 4, 5])

    # # Iterate in multiples of A + 1 until 2X
    def test_multiples_plus_one(self):
        result = multiples.multiples(1, 5, 1, 2)
        self.assertListEqual(result, [2, 4, 6, 8, 10])

    # # Iterate in multiples of A + 2 until 3X
    def test_multiples_plus_two(self):
        result = multiples.multiples(1, 5, 2, 3)
        self.assertListEqual(result, [3, 6, 9, 12, 15])

    def test_zero(self):
        result = multiples.multiples(0, 0)
        self.assertListEqual(result, [])

if __name__ == '__main__':
    unittest.main()