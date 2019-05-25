
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        i = 2
        s = "11"
        while i < n:
            j = 0
            next_s = ""
            count = 1
            while j < len(s) - 1:
                # print(i, next_s)
                if s[j] == s[j + 1]:
                    count += 1
                else:
                    next_s += str(count) + s[j]
                    count = 1
                j += 1
            next_s += str(count) + s[j]
            s = next_s
            i += 1
        return s

s = Solution()

print(s.countAndSay(1))
print(s.countAndSay(2))
print(s.countAndSay(3))
print(s.countAndSay(4))
print(s.countAndSay(30))