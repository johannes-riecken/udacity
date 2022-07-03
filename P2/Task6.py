class TrieNode:
    """Represents a single node in the Trie"""
    def __init__(self):
        self.children = []

    def insert(self, char):
        self.children.append(char)

class Trie:
    """The Trie itself containing the root node and insert/find functions"""
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.rootNode = TrieNode()

    def insert(self, word):
        # Add a word to the Trie
        node = self.rootNode
        while len(word) > 0:
            char, word = word[0], word[1:]




    def find(self, prefix):
        # Find the Trie node that represents this prefix
        pass
