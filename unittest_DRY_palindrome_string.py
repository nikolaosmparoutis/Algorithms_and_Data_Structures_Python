import unittest
from palindrome_string import isPalindrome


# DRY approach using context manager on testing
class MyTestCase(unittest.TestCase):
    def expectEqual(self, first, second, msg=None):
        with self.subTest():
            self.assertEqual(first, second, msg)


class TestPalindromeString(MyTestCase):
    def test_palindrome(self):
        self.assertEqual(isPalindrome(""), False)
        self.assertEqual(isPalindrome("a"), True)
        self.assertEqual(isPalindrome("ab"), False)
        self.assertEqual(isPalindrome("aba"), True)
        self.assertEqual(isPalindrome("abb"), False)
        self.assertEqual(isPalindrome("abba"), True)
        self.assertEqual(isPalindrome("abOba"), True)
        self.assertEqual(isPalindrome("abOkba"), False)
        self.assertEqual(isPalindrome("abcdcba"), True)
        self.assertEqual(isPalindrome("abcdefghihgfeddcba"), False)


if __name__ == '__main__':
    unittest.main()
