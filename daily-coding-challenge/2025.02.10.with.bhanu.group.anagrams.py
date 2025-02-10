# words -> [listen, netils, teinls]
# [[listen, netils, teinls], [cat], [bob], [net]] 4 groups
# question 1: return all groups of strings by anagrams: [[listen, netils, teinls], [cat], [bob], [net]]
# question 2: reverse order of groups: [[teinls, netils, listen], [cat], [bob], [net]]
# question 3: reverse order of words that are anagrams of each other

"""
find words with same len:
if there are 2 or more words with same len, prase one of them and create a hash map.
    walk thru rest of thw words, and loop thru the hashmap and see if find an anagram

    [[[listen, loc], [netils, loc], teinls], [cat], [bob], [net]]

"""

from collections import defaultdict

def anagramQ1(words: list[str]) -> list[list[str]]:
    anagrams: dict[str, list[str]] = defaultdict(list)
    for word in words:
        anagrams["".join(sorted(word))].append(word)

    return list(anagrams.values())

def anagramQ2(words: list[str]) -> list[list[str]]:
    l = anagramQ1(words)
    for group in l:
        group.reverse()

    return l

def anagramQ3(words: list[str]) -> list[str]:
    anagrams: dict[str, list[int]] = defaultdict(list)
    for i, word in enumerate(words):
        anagrams["".join(sorted(word))].append(i)

    print (anagrams)
    for group in anagrams.values():
        left = 0
        right = len(group) - 1
        while left < right:

            # listen, 0  teinls, 5
            u, v = group[left], group[right]
            words[u], words[v] = words[v], words[u]

            left +=1
            right -=1

    return words

# defaultdict(<class 'list'>, {'eilnst': [('listen', 0), ('netils', 1), ('teinls', 5)], 'act': ['cat', 'tac'], 'bbo': ['bob', 'obb'], 'ent': ['net']})
#                                        [('teinls', 5), ('netils', 1), ('listen', 0)]

w1 = ["listen", "netils", "cat", "bob", "net", "teinls", "tac", "obb"]
#      listen    netils                         teinls
#      teinls    netils   tac    obb            listen
#                          cat                            tac
#                          tac    obb                         cat

# final output
#    ["teinls", "netils", "tac", "obb", "net", "listen", "cat", "bob"]

# print(anagramQ1(w1))
# print(anagramQ2(w1))
print(w1)
print(anagramQ3(w1))