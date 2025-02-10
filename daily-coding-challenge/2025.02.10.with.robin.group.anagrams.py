# words -> [listen, netils, cat, bob, net, teinls]
# [[listen, netils, teinls], [cat], [bob], [net]] 4 groups
# question 1: return 4
# question 2: return [[teinls, netils, listen], [cat], [bob], [net]]

from collections import defaultdict

def countLetters(word: str) -> list[int]:
    count = [0 for _ in range(26)]
    for letter in word:
        count[ord(letter) - ord('a')] += 1

    return count

# question 1
def anagramQ1(words: list[str]) -> list[list[str]]:
    anagrams: dict[tuple[int, ...], list[str]] = defaultdict(list)

    for word in words:
        anagrams[tuple(countLetters(word))].append(word)

    return list(anagrams.values())

def anagramQ2(words: list[str]) -> list[list[str]]:
    return [list(reversed(group)) for group in anagramQ1(words)]

# question 3: reverse the order in the original list of words that are anagrams
# anagramQ3(w1) == ["teinls", "netils", "tac", "obb", "net", "listen", "cat", "bob"]
def anagramQ3(words: list[str]) -> list[str]:
    anagrams: dict[tuple[int, ...], list[int]] = defaultdict(list)

    for index, word in enumerate(words):
        anagrams[tuple(countLetters(word))].append(index)

    for group in anagrams.values():
        for i in range(len(group)//2):
            i1, i2 = group[i], group[-i-1]
            words[i1], words[i2] = words[i2], words[i1]

    return words

w1 = ["listen", "netils", "cat", "bob", "net", "teinls", "tac", "obb"]
assert(anagramQ1(w1) == [["listen", "netils", "teinls"], ["cat", "tac"], ["bob", "obb"], ["net"]])
assert(anagramQ3(w1) == ["teinls", "netils", "tac", "obb", "net", "listen", "cat", "bob"])
# print(w1)
# print(anagramQ3(w1))