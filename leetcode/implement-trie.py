class Trie:
    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        c = self.head
        for letter in word:
            i = ord(letter) - 97 # ord("a")
            if c.next[i] is None:
                c.next[i] = TrieNode()
            c = c.next[i]
        c.end = True

    def getNode(self, word: str) -> 'TrieNode':
        c = self.head
        for letter in word:
            i = ord(letter) - 97
            if c.next[i] is None:
                return None
            c = c.next[i]
        return c

    def search(self, word: str) -> bool:
        node = self.getNode(word)
        return node is not None and node.end

    def startsWith(self, prefix: str) -> bool:
        return self.getNode(prefix) is not None

class TrieNode:
    def __init__(self):
        self.end = False
        self.next = [None] * 26

t = Trie()

for word in ["apple", "app", "sad", "sadder"]:
    t.insert(word)

assert t.search("a") ==  False
assert t.search("apple") == True
assert t.search("apples") == False
assert t.startsWith("app") == True
assert t.startsWith("sad") == True
assert t.startsWith("sadde") == True
