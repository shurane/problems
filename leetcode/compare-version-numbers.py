class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")

        i = 0
        while i < len(v1) and i < len(v2):
            left = int(v1[i])
            right = int(v2[i])

            if left > right:
                return 1
            elif right > left:
                return -1

            i += 1

        if len(v1) > len(v2):
            for j in range(i, len(v1)):
                subversion = int(v1[j])
                if subversion > 0:
                    return 1
        elif len(v2) > len(v1):
            for j in range(i, len(v2)):
                subversion = int(v2[j])
                if subversion > 0:
                    return -1

        return 0

s = Solution()
assert s.compareVersion("1", "1") == 0
assert s.compareVersion("1", "2") == -1
assert s.compareVersion("2", "1") == 1
assert s.compareVersion("1.01", "1.001") == 0
assert s.compareVersion("1.0", "1.0.0") == 0
assert s.compareVersion("0.1", "1.1") == -1
assert s.compareVersion("1.1", "0.1") == 1
assert s.compareVersion("1.1", "1.0.0.0.0.15") == 1

assert s.compareVersion("1.1.1.1.1.1", "1.1.1.1.1.1") == 0

assert s.compareVersion("1.1.1.1.1.0", "1.1.1.1.1.1") == -1
assert s.compareVersion("1.1.1.1.1", "1.1.1.1.1.1") == -1

assert s.compareVersion("1.1.1.1.1.1", "1.1.1.1.1.0") == 1
assert s.compareVersion("1.1.1.1.1.1", "1.1.1.1.1") == 1
