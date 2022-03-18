class Solution:
    # this is so not intuitive. Had to look at the solution.
    # It kind of makes sense though. sliding window + evicting weaker values from the stack
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        m = dict()
        for i, l in enumerate(s): m[l] = i

        for i, l in enumerate(s):
            if l not in seen:
                while stack and l < stack[-1] and i < m[stack[-1]]:
                    seen.remove(stack[-1])
                    stack.pop()
                seen.add(l)
                stack.append(l)

        return "".join(stack)

s = Solution()

assert s.removeDuplicateLetters("bca") == "bca"
assert s.removeDuplicateLetters("bcab") == "bca"
assert s.removeDuplicateLetters("bcabc") == "abc"
assert s.removeDuplicateLetters("cbacdcbc") == "acdb"
