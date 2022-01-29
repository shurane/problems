class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        first, rest = A[0], A[1:]

        common = []
        for letter in first:
            if all(letter in word for word in rest):
                common.append(letter)
                rest = [word.replace(letter, "", 1) for word in rest]
        return common

# 6 minutes