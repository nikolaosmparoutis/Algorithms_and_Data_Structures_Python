import unittest
import largest_number_range


# DRY approach using context manager on testing
class MyTestCase(unittest.TestCase):
    def expectEqual(self, first, second, msg=None):
        with self.subTest():
            self.assertEqual(first, second, msg)


class TestLargestNumberRange(unittest.TestCase):
    def test_something(self):
        self.assertEqual(largest_number_range.largestRange([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]), [0, 7])
        self.assertEqual(largest_number_range.largestRange([1, 1]), [1, 1])
        self.assertEqual(largest_number_range.largestRange([-3, 5, 6, 7, -4, -5 ]), [-5, -3] )
        self.assertEqual(largest_number_range.largestRange([4, 2, 1, 3]), [1, 4])
        self.assertEqual(largest_number_range.largestRange([8, 4, 2, 10, 3, 6, 7, 9, 1]), [6, 10] )
        self.assertEqual(largest_number_range.largestRange([-1, 0, 1]), [-1, 1])

if __name__ == '__main__':
    unittest.main()
