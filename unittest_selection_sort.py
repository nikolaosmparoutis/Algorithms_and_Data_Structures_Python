import unittest
import selection_sort as s
class MyTestCase(unittest.TestCase):
    def expectEqual(self, first, second, msg=None):
        with self.subTest():
            self.assertEqual(first, second, msg)


class MyTestCase(unittest.TestCase):
    def test_selection_sort(self):
        self.assertEqual(s.selectionSort([8, 5, 2, 9, 5, 6, 3]),[2, 3, 5, 5, 6, 8, 9])
        self.assertEqual(s.selectionSort([1]),[1])
        self.assertEqual(s.selectionSort([]),[])
        self.assertEqual(s.selectionSort([7, 4, -10, 6, -10, -9]),[-10, -10, -9, 4, 6, 7])


if __name__ == '__main__':
    unittest.main()
