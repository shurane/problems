from typing import Dict

class Solution:
    def originalDigits(self, s: str) -> str:
        numberCounts = [counter(n) for n in ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]]
        sCount = counter(s)
        results = [0] * 10

        """

        is this a linear combination of vectors to a target? just count up the letters for 's' and each of the numbers
        https://en.wikipedia.org/wiki/Linear_combination
        kind of feels like a polynomial problem, but I guess that's what linear combination is -- see unit vectors for Ax + By = result, etc
        without an algorithm, I could try to use intuition instead
        could go from numbers that have unique letters - zero (z), two (w), four (u), six (x), eight (g) -- strangely all even
        then do ones that are unique                   - one (o), three (thr), five (f), seven (s)
        then leftovers...                              - nine

        ----

        from looking at other solutions, the other numbers can be represented in terms of the unique ones
        see https://leetcode.com/problems/reconstruct-original-digits-from-english/discuss/
        i.e.
        zero    = z
        two     = w
        four    = u
        six     = x
        eight   = g
        seven   = s - x             (s - 6)
        five    = f - u             (f - 4)
        three   = t - w - g         (t - 2 - 8)
        one     = o - z - w - u     (o - 0 - 2 - 4)
        nine    = i - x - g - f + u (i - 6 - 8 - (f - 4))
        """

        results[0] = sCount.get("z", 0)
        if results[0]:
            sCount["z"] -= results[0]
            sCount["e"] -= results[0]
            sCount["r"] -= results[0]
            sCount["o"] -= results[0]
        results[2] = sCount.get("w", 0)
        if results[2]:
            sCount["t"] -= results[2]
            sCount["w"] -= results[2]
            sCount["o"] -= results[2]
        results[4] = sCount.get("u", 0)
        if results[4]:
            sCount["f"] -= results[4]
            sCount["o"] -= results[4]
            sCount["u"] -= results[4]
            sCount["r"] -= results[4]
        results[6] = sCount.get("x", 0)
        if results[6]:
            sCount["s"] -= results[6]
            sCount["i"] -= results[6]
            sCount["x"] -= results[6]
        results[8] = sCount.get("g", 0)
        if results[8]:
            sCount["e"] -= results[8]
            sCount["i"] -= results[8]
            sCount["g"] -= results[8]
            sCount["h"] -= results[8]
            sCount["t"] -= results[8]
        results[1] = sCount.get("o", 0)
        if results[1]:
            sCount["o"] -= results[1]
            sCount["n"] -= results[1]
            sCount["e"] -= results[1]
        results[3] = sCount.get("r", 0)
        if results[3]:
            sCount["t"] -= results[3]
            sCount["h"] -= results[3]
            sCount["r"] -= results[3]
            sCount["e"] -= results[3]
            sCount["e"] -= results[3] # repeat
        results[5] = sCount.get("f", 0)
        if results[5]:
            sCount["f"] -= results[5]
            sCount["i"] -= results[5]
            sCount["v"] -= results[5]
            sCount["e"] -= results[5]
        results[7] = sCount.get("s", 0)
        if results[7]:
            sCount["s"] -= results[7]
            sCount["e"] -= results[7]
            sCount["v"] -= results[7]
            sCount["e"] -= results[7] # repeat
            sCount["n"] -= results[7]
        results[9] = sCount.get("i", 0)

        return ("0" * results[0] +
                "1" * results[1] +
                "2" * results[2] +
                "3" * results[3] +
                "4" * results[4] +
                "5" * results[5] +
                "6" * results[6] +
                "7" * results[7] +
                "8" * results[8] +
                "9" * results[9] )

def counter(s: str) -> Dict[str, int]:
    m = dict()
    for letter in s:
        if letter not in m:
            m[letter] = 0
        m[letter] += 1
    return m

s = Solution()

assert s.originalDigits("zero") == "0"
assert s.originalDigits("zerozerozerotwo") == "0002"
assert s.originalDigits("owoztneoer") == "012"
assert s.originalDigits("fviefuro") == "45"