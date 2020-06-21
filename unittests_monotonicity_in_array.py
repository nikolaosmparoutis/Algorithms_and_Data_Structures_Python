
import is_monotonic_array
import unittest


class Test_is_monotonic_array(unittest.TestCase):
    def Test_Case_1(self):
        array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
        expected = True
        actual = is_monotonic_array.isMonotonic(array)
        self.assertEqual(actual, expected)

    def Test_Case_2(self):
        array = []
        expected = True
        actual = is_monotonic_array.isMonotonic(array)
        self.assertEqual(actual, expected)

    def Test_Case_3(self):
        array = [1]
        expected = True
        actual = is_monotonic_array.isMonotonic(array)
        self.assertEqual(actual, expected)

    def Test_Case_4(self):
        array = [1, 2]
        expected = True
        actual = is_monotonic_array.isMonotonic(array)
        self.assertEqual(actual, expected)

    def Test_Case_5(self):
        array = [2, 1]
        expected = True
        actual = is_monotonic_array.isMonotonic(array)
        self.assertEqual(actual, expected)

    def Test_Case_6(self):
        array = [1, 5, 10, 1100, 1101, 1102, 9001]
        expected = True
        actual = is_monotonic_array.isMonotonic(array)
        self.assertEqual(actual, expected)

    def Test_Case_7(self):
        array = [-1, -5, -10, -1100, -1101, -1102, -9001]
        expected = True
        actual = is_monotonic_array.isMonotonic(array)
        self.assertEqual(actual, expected)

    def Test_Case_8(self):
        array = [-1, -5, -10, -1100, -900, -1101, -1102, -9001]
        expected = False
        actual = is_monotonic_array.isMonotonic(array)
        self.assertEqual(actual, expected)

    def Test_Case_9(self):
        array =[1, 2, 0]
        expected = False
        actual = is_monotonic_array.isMonotonic(array)
        self.assertEqual(actual, expected)

    def Test_Case_10(self):
        array =[1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 7, 9, 10, 11]
        expected = False
        actual = is_monotonic_array.isMonotonic(array)
        self.assertEqual(actual, expected)

    def Test_Case_11(self):
        array =[1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 11]
        expected = True
        actual = is_monotonic_array.isMonotonic(array)
        self.assertEqual(actual, expected)

    def Test_Case_12(self):
        array =[-1, -1, -2, -3, -4, -5, -5, -5, -6, -7, -8, -7, -9, -10, -11]
        expected = False
        actual = is_monotonic_array.isMonotonic(array)
        self.assertEqual(actual, expected)

    def Test_Case_13(self):
        array =[-1, -1, -2, -3, -4, -5, -5, -5, -6, -7, -8, -8, -9, -10, -11]
        expected = True
        actual = is_monotonic_array.isMonotonic(array)
        self.assertEqual(actual, expected)

    def Test_Case_14(self):
        array =[-1, -1, -1, -1, -1, -1, -1, -1]
        expected = True
        actual = is_monotonic_array.isMonotonic(array)
        self.assertEqual(actual, expected)

    def Test_Case_15(self):
        array =[1, 2, -1, -2, -5]
        expected = False
        actual = is_monotonic_array.isMonotonic(array)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
