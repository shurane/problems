from typing import List

class WordFilter:
    # see https://leetcode.com/problems/prefix-and-suffix-search/discuss/110053/Python-few-ways-to-do-it-with-EXPLANATIONS!-U0001f389
    # pretty clever solution. And so much faster than going up and down a prefix and suffix Trie. Thank you yangshun and 8939123

    def __init__(self, words: List[str]):
        self.inputs = dict()
        for index, word in enumerate(words):
            for i in range(len(word) + 1):
                for j in range(len(word) + 1):
                    self.inputs[word[:i] + "." + word[j:]] = index
        # print(self.inputs)

    def f(self, prefix: str, suffix: str) -> int:
        return self.inputs.get(prefix + "." + suffix, -1)

w = WordFilter(["apple", "aranciata", "avocado", "banana", "barley", "beans", "broccoli", "carrot", "cauliflower", "celery"])
assert w.f("a", "e") == 0
assert w.f("a", "a") == 1
assert w.f("a", "o") == 2
assert w.f("av", "do") == 2
assert w.f("b", "a") == 3
assert w.f("ba", "na") == 3

w2 = WordFilter(["apple"])
assert w2.f("a", "e") == 0