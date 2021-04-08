from typing import List
import unittest

m = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        output = []
        for d in digits:
            newOutput = []
            for l in m[d]:
                if output:
                    for word in output:
                        newOutput.append(word + l)
                # seed output for first time
                else:
                    newOutput.append(l)
            output = newOutput
        # print(digits, output)
        return output

s = Solution()
case = unittest.TestCase()

case.assertCountEqual(s.letterCombinations(""), [])
case.assertCountEqual(s.letterCombinations("2"), ["a", "b", "c"])
case.assertCountEqual(s.letterCombinations("3"), ["d", "e", "f"])
case.assertCountEqual(s.letterCombinations("4"), ["g", "h", "i"])
case.assertCountEqual(s.letterCombinations("5"), ["j", "k", "l"])
case.assertCountEqual(s.letterCombinations("6"), ["m", "n", "o"])
case.assertCountEqual(s.letterCombinations("7"), ["p", "q", "r", "s"])
case.assertCountEqual(s.letterCombinations("8"), ["t", "u", "v"])
case.assertCountEqual(s.letterCombinations("9"), ["w", "x", "y", "z"])
case.assertCountEqual(s.letterCombinations("23"), ["ad","ae","af","bd","be","bf","cd","ce","cf"])