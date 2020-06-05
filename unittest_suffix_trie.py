
import suffix_trie
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        trie = suffix_trie.SuffixTrie("babc")
        expected = {
            "c": {"*": True},
            "b": {"c": {"*": True}, "a": {"b": {"c": {"*": True}}}},
            "a": {"b": {"c": {"*": True}}},
        }
        self.assertEqual(trie.root, expected)
        self.assertTrue(trie.contains("abc"))
