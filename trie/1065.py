class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.is_word = True        
        

class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        res = []
        for i in range(len(text)):
            j = i
            node = trie.root
            while j < len(text) and text[j] in node.children:
                node = node.children[text[j]]
                if node.is_word:
                    res.append([i, j])
                j += 1
        return res