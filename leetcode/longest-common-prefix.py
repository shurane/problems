class Solution:
    # not particularly elegant
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        i = 0
        matching = True
        while i < len(strs[0]) and matching:
            j = 0
            while j < len(strs) - 1:
                if i >= len(strs[j]) or i >= len(strs[j+1]):
                    matching = False
                    break
                elif strs[j][i] != strs[j+1][i]:
                    matching = False
                    break
                j += 1

            if matching:
                i += 1

        return strs[0][:i]

