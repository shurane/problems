from typing import List

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        # this is some low-key awful looking code. There must be a way to clean it up.

        results = []
        ss = "".join([l for l in s if l not in "() "])
        n = len(ss)
        for i in range(1, n):
            left = ss[:i].strip()
            right = ss[i:].strip()
            # print("whole", left, right, int(left) == 0 and len(left) > 1, int(right) == 0 and len(right) > 1)
            if int(left) == 0 and len(left) > 1 or int(right) == 0 and len(right) > 1:
                continue

            if not (left.startswith("0") and int(left) > 0 or right.startswith("0") and int(right) > 0):
                results.append(f"({left}, {right})")

            # decimal point on left
            for j in range(1, len(left)):
                integerpart = left[:j]
                fractionalpart = left[j:]
                # print(f"left fraction {integerpart:3} {fractionalpart:3} right          {right:3}")
                if integerpart.startswith("00") or integerpart.startswith("0") and int(integerpart) > 0 \
                    or fractionalpart.endswith("0") \
                    or right.startswith("0") and int(right) > 0 \
                    or int(fractionalpart) == 0:
                    continue
                results.append(f"({integerpart}.{fractionalpart}, {right})")

            # decimal point on right
            for k in range(1, len(right)):
                integerpart = right[:k]
                fractionalpart = right[k:]
                # print(f"left          {left:3}     right fraction {integerpart:3} {fractionalpart:3}")
                if integerpart.startswith("00") or integerpart.startswith("0") and int(integerpart) > 0 \
                    or fractionalpart.endswith("0") \
                    or left.startswith("0") and int(left) > 0 \
                    or int(fractionalpart) == 0:
                    continue
                results.append(f"({left}, {integerpart}.{fractionalpart})")


            # decimal point on both
            for j in range(1, len(left)):
                for k in range(1, len(right)):
                    lint = left[:j]
                    lfrac = left[j:]
                    rint = right[:k]
                    rfrac = right[k:]
                    if lint.startswith("00") or lint.startswith("0") and int(lint) > 0 or int(lfrac) == 0 or \
                       rint.startswith("00") or rint.startswith("0") and int(rint) > 0 or int(rfrac) == 0 or \
                       lfrac.endswith("0") or rfrac.endswith("0"):
                       continue
                    results.append(f"({lint}.{lfrac}, {rint}.{rfrac})")

        # print(results)
        return results

def sortedCompare(a, b):
    # print(sorted(a))
    # print(sorted(b))
    return sorted(a) == sorted(b)

s = Solution()
assert sortedCompare(s.ambiguousCoordinates("(123)"),["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"])
assert sortedCompare(s.ambiguousCoordinates("(00011)"), ["(0.001, 1)", "(0, 0.011)"])
assert sortedCompare(s.ambiguousCoordinates("(100)"), ["(10, 0)"])
assert sortedCompare(s.ambiguousCoordinates("(0123)"), ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"])
assert sortedCompare(s.ambiguousCoordinates("(0010)"), ["(0.01, 0)"])