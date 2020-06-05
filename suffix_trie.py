class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    # T=O(n^2) | space O(n^2)
    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.insertSubstringStartingAt(i, string)

    def insertSubstringStartingAt(self, i, string):
        node = self.root
        print(node)
        for j in range(i, len(string)):
            letter = string[j]
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.endSymbol] = True

    # T=O(m) m = string or substring length we are looking | space O(1)
    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        if self.endSymbol in node:
            return True
        else:
            return False


if __name__ == '__main__':
    trie_str = "babc"
    st = SuffixTrie(trie_str)
    found = st.contains("abc")
    print("found =", found)


