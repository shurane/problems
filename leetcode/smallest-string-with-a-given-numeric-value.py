class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        if n == 1 and k <= 27:
            return chr(k + 96)
        else:
            value = min(26, k - n + 1)
            letter = chr(value + 96)
            result = self.getSmallestString(n - 1, k - value) + letter
            # print(n, result)
            return result

    # string is basically 'a' * number + '[b-y]' + 'z' * number
    def getSmallestStringIterative(self, n: int, k: int) -> str:
        res = []
        while n > 0:
            # k - n + 1 is how many spots to reserve with 'a' in the beginning of the string
            value = min(26, k - n + 1)
            letter = chr(value + 96)
            res.append(letter)
            n -= 1
            k -= value

        return "".join(reversed(res))

    # https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/discuss/944529/Python-without-any-loop
    # https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/discuss/946553/Correct-simple-Python-solution-without-loop
    def getSmallestStringFast(self, n: int, k: int) -> str:
        q, r = divmod(k - n, 25)
        if q == n:
            # print("z" * q)
            return "z" * q

        res = "a" * (n-q-1) + chr(r + 97) + "z" * q
        # print(res)
        return res

s = Solution()

testcases = [[1,1,"a"],
             [1,25,"y"],
             [1,26,"z"],
             [5,26,"aaaav"],
             [3,27,"aay"],
             [5,73,"aaszz"],
             [5,5,"aaaaa"],
             [5,130,"zzzzz"]]

for n, k, expected in testcases:
    assert s.getSmallestString(n, k) == expected
    assert s.getSmallestStringIterative(n, k) == expected
    assert s.getSmallestStringFast(n, k) == expected

big_testcases = [[91339, 91339, "a" * 91339],
                 [91339, 91339 + 1, "a" * 91338 + "b"],
                 [91339, 112545, "a" * 90490 + "g" + "z" * 848 ],
                 [91339, 91339 * 26 - 1, "y" + "z" * 91338],
                 [91339, 91339 * 26, "z" * 91339]]

for n, k, expected in big_testcases:
    assert s.getSmallestStringIterative(n, k) == expected
    assert s.getSmallestStringFast(n, k) == expected

