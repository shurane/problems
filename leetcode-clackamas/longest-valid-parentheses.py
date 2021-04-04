# from colorama import init, Fore
# init()

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0

        # similar to longest-palindromic-substring
        longest = ""
        depths = dict()
        i = 0
        while i < len(s) - 1:
            l, r = i, i + 2
            partial = s[l:r]

            if partial == "()":
                while l >= 0 and r <= len(s):
                    # print(f"{l:3} {r:3}", f"{s[:l]}{Fore.BLUE}{s[l:r]}{Fore.RESET}{s[r:]} length = {len(partial):3}")
                    depths[r] = l
                    if r > i:
                        i = r
                    if len(partial) > len(longest):
                        longest = partial

                    # check if string to the left can be connected to partial
                    if l in depths:
                        # print("extending on left", i, depths[i])
                        l = depths[l]
                    # check if () is to the right of partial
                    elif r + 2 <= len(s) and s[r:r + 2] == "()":
                        r += 2
                    # check if ( is on the left and ) is on the right of partial
                    elif l - 1 >= 0 and r < len(s) and s[l - 1] == "(" and s[r] == ")":
                        l -= 1
                        r += 1
                    # otherwise, not possible to create a string, so break
                    else:
                        break

                    partial = s[l:r]
            i += 1

        # from here, we could probably store the different longest valid strings we found, and in the end, assemble them together to find the actual longest
        # doesn't seem enough, though.... what other case is it missing?
        # nevermind -- instead of storing the longest valid string, we should store the end indices of all valid strings

        # Seems like a slow solution, but it works. What is the runtime?
        # Can't be O(n**2) since we don't revisit the left side of the string and store the results.
        # Although we do keep revisiting the right side of the string and don't store the results, so it looks like it is O(n**2) unless we skip it somehow.
        # Worst case input is () * n -- results in O(n**2) runtime.
        # We can fix that by checking if a valid partial string with r > i, then replace i with r

        # print(depths)
        return len(longest)

s = Solution()

assert s.longestValidParentheses("") == 0
assert s.longestValidParentheses("(()") == 2
assert s.longestValidParentheses(")()())") == 4
assert s.longestValidParentheses(")(()())") == 6
assert s.longestValidParentheses("(()())") == 6
assert s.longestValidParentheses("(()())()") == 8
assert s.longestValidParentheses("()(()())()") == 10
assert s.longestValidParentheses("(())(())") == 8
assert s.longestValidParentheses("((())(()))") == 10
assert s.longestValidParentheses(")(((((()())()()))()(()))(") == 22
assert s.longestValidParentheses("()(())((()))(((())))((((()))))") == 30
assert s.longestValidParentheses("((()())(()()))((()())(()()))") == 28
assert s.longestValidParentheses("((()())(()()))((()())(()()))((()())(()()))") == 42
assert s.longestValidParentheses("()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()") == 100
assert s.longestValidParentheses(")(()(()(((())(((((()()))((((()()(()()())())())()))()()()())(())()()(((()))))()((()))(((())()((()()())((())))(())))())((()())()()((()((())))))((()(((((()((()))(()()(())))((()))()))())") == 132