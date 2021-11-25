class Solution:
    def decodeString(self, s: str) -> str:
        return helper(s, 0, len(s))

def helper(s: str, l:int, r:int):
    result = ""
    while l < r:
        if s[l] in "0123456789":
            i = l + 1
            while s[i] != "[":
                i += 1
            j = i + 1
            stack = 1
            while stack > 0:
                if s[j] == "[":
                    stack += 1
                elif s[j] == "]":
                    stack -= 1
                j += 1
            j -= 1 # we are 1 char past the last "]", so decrement j by 1
            count = int(s[l:i])
            inner = helper(s, i+1, j) * count
            result += inner
            l = j
        else:
            result += s[l]
        l += 1
    # print(result)
    return result

s = Solution()

assert s.decodeString("a") == "a"
assert s.decodeString("abc") == "abc"
assert s.decodeString("a1[b]2[c]3[d]4[e]") == "abccdddeeee"
assert s.decodeString("2[a2[b2[c]]]") == "abccbccabccbcc"
assert s.decodeString("10[a]") == "a" * 10
assert s.decodeString("30[a]") == "a" * 30
assert s.decodeString("10[10[a]]") == "a" * 10 * 10
assert s.decodeString("100[a]") == "a" * 100
assert s.decodeString("3[a]2[bc]") == "aaabcbc"
assert s.decodeString("3[a2[c]]") == "accaccacc"
assert s.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"
assert s.decodeString("abc3[cd]xyz") == "abccdcdcdxyz"