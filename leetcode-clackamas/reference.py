# from dataclasses import dataclass
# @dataclass
# class Paren:
#     index: int = None
#     char: str = None

# from typing import NamedTuple
# class Paren(NamedTuple):
#     index: int = None
#     char: str = None

# thought this would be useful for longest-string-chain, but it was for a different type of problem
# def diff(w1, w2):
#     i = j = count = 0
#     w1, w2 = sorted(w1), sorted(w2)

#     while i < len(w1) and j < len(w2):
#         if w1[i] < w2[j]:
#             count += 1
#             i += 1
#         elif w1[i] > w2[j]:
#             count += 1
#             j += 1
#         else:
#             i += 1
#             j += 1
#     count += len(w1) - i + len(w2) - j
#     return count

# assert diff("abc", "abc") == 0
# assert diff("a", "ba") == 1
# assert diff("abc", "abcd") == 1
# assert diff("abc", "abcde") == 2
# assert diff("abc", "xyz") == 6 # is this correct? Not sure what the value should be, but it doesn't matter for this problem