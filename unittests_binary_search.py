import unittest
from  binary_search import binarySearch

# DRY approach using context manager on testing
class MyTestCase(unittest.TestCase):
    def expectEqual(self, first, second, msg=None):
        with self.subTest():
            self.assertEqual(first, second, msg)


class TestCase(MyTestCase):
    def test_binary_search(self):
        self.assertEqual(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33), 3)
        self.assertEqual(binarySearch([1, 5, 23, 111],111),3)
        self.assertEqual(binarySearch([1, 5, 23, 111],5),1)
        self.assertEqual(binarySearch([5, 23, 111],3),-1)
        self.assertEqual(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73],72),8)
        self.assertEqual(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73],70),-1)
        self.assertEqual(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355],355),10)
        self.assertEqual(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355],354),-1)
        self.assertEqual(binarySearch([1, 5, 23, 111],120),-1)


if __name__ == '__main__':
    unittest.main()
