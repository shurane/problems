import re

class Solution:
    def isNumber(self, s: str) -> bool:
        # this works, but it would be nice to be able to solve this in only 1 loop. My solution iterates it several times
        # an example of 1 loop using DFA: https://leetcode.com/problems/valid-number/discuss/23728/A-simple-solution-in-Python-based-on-DFA
        # a clever example of 1 loop by using booleans for states (without a DFA):  https://leetcode.com/problems/valid-number/discuss/173977/Python-with-simple-explanation
        espies = re.split("[eE]", s)
        # print("espies", s, espies)
        if len(espies) > 2: return False
        elif len(espies) == 2:
            # print("espies", isDecimal(espies[0]), isSignedInteger(espies[1]))
            return isDecimal(espies[0]) and isSignedInteger(espies[1])
        return isDecimal(s)

digits = "0123456789"
signs = "-+"
digitsigns = digits + signs
def isInteger(s): return s != "" and all(l in digits for l in s)
def isSignedInteger(s):
    return len(s) > 0 and s[0] in signs and isInteger(s[1:]) or isInteger(s)

def isDecimal(s):
    if not s: return False

    digitcount = 0
    decimalcount = 0
    for i, l in enumerate(s):
        if l in signs:
            if i != 0 or i == len(s) - 1: return False
        elif l == ".":
            if i == 0 and i == len(s) - 1: return False
            decimalcount += 1
        elif l not in digits: return False
        else:
            digitcount += 1
    return decimalcount <= 1 and digitcount > 0

# def isIntegerE(s):
#     if not s: return False
#     ecount = 0
#     for i, l in enumerate(s):
#         if l in signs:
#             if i != 0 or i == len(s) - 1: return False
#         elif l in "eE":
#             if i == 0 or i == len(s) - 1: return False
#             ecount += 1
#         elif l not in digits: return False
#     return ecount <= 1

s = Solution()

for value in ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]:
    assert s.isNumber(value) == True

for value in ["", "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53", ".", "4e+", "+."]:
    assert s.isNumber(value) == False