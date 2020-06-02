import product_sums
import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test_1 = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
        self.assertEqual(product_sums.productSum(test_1), 12)

        test_2 = [[[[[5]]]]]
        self.assertEqual(product_sums.productSum(test_2),600)

        test_3 = 'asdsasd'
        self.assertEqual(product_sums.productSum(test_3),Exception)

        test_4 = ''
        self.assertEqual(product_sums.productSum(test_4), 0)
