powers = set()
for i in range(32):
    num = 2**i
    digits = [int(d) for d in str(num)]
    sortedDigits = tuple(sorted(digits))
    # print(f"2**{i}", num, digits, sortedDigits)
    powers.add(sortedDigits)

# print(powers)

class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        digits = [int(d) for d in str(N)]
        sortedDigits = tuple(sorted(digits))
        # print(sortedDigits, sortedDigits in powers)
        return sortedDigits in powers

s = Solution()
assert s.reorderedPowerOf2(821) == True