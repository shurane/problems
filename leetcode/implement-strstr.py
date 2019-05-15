class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        i = 0
        while i < len(haystack) - len(needle) + 1:
            j = 0
            matching = True
            while j < len(needle):
                if haystack[i + j] != needle[j]:
                    matching = False
                    break
                j += 1
            if matching:
                return i
            i += 1
        
        return -1
        