from typing import List
from bisect import insort_left, bisect_left

# https://albertauyeung.github.io/2020/06/15/python-trie.html
class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.index = -1
        self.children = {}

    def __repr__(self):
        return f"TrieNode({self.char}, end={self.is_end})"

class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word, index=-1):
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.is_end = True
        if index != -1:
            node.index = index

    def query(self, prefix):
        node = self.root

        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return []

        # modified to not use DFS
        results = []
        q = [(prefix, node)]
        # print("before", q)
        while q:
            p, n = q.pop()
            # print("q", f"{p:10}", n, "next:", n.children.keys())
            if n.is_end:
                if n.index != -1:
                    insort_left(p, n.index)
                else:
                    insort_left(results, p)

            for key in n.children:
                q.append((p + key, n.children[key]))

        return results

class Solution:
    def suggestedProductsTrie(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Based on the solutions, it seems like this is an overkill way to solve this problem
        t = Trie()
        for product in products:
            t.insert(product)

        results = []
        for i in range(1, len(searchWord) + 1):
            pre = searchWord[:i]
            matches = t.query(pre)
            results.append(matches[:3])

        # print(results)
        return results

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # https://leetcode.com/problems/search-suggestions-system/discuss/436674/C%2B%2BJavaPython-Sort-and-Binary-Search-the-Prefix
        products.sort()
        results = []
        prefix = ""
        i = 0

        for c in searchWord:
            prefix += c
            i = bisect_left(products, prefix)
            matches = []
            for word in products[i:i+3]:
                if word.startswith(prefix):
                    matches.append(word)
            results.append(matches)
        return results

s = Solution()

r1 = s.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse")
assert r1 == [
    ["mobile","moneypot","monitor"],
    ["mobile","moneypot","monitor"],
    ["mouse","mousepad"],
    ["mouse","mousepad"],
    ["mouse","mousepad"]
]

r2 = s.suggestedProducts(["havana"], "havana")
assert r2 == [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

r3 = s.suggestedProducts(["bags","baggage","banner","box","cloths"], "bags")
assert r3 == [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]

r3_ = s.suggestedProducts(["bags","baggage","banner","box","cloths"], "b")
assert r3_ == [["baggage", "bags", "banner"]]

r4 = s.suggestedProducts(["havana"], "tatiana")
assert r4 == [[],[],[],[],[],[],[]]
