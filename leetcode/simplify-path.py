class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = []

        for part in path.split("/"):
            if part == "" or part == ".":
                continue
            elif part == "..":
                if parts:
                    parts.pop()
            else:
                parts.append(part)

        # print(parts, "/" + "/".join(parts))
        return "/" + "/".join(parts)

    def simplifyPathLessIfs(self, path: str) -> str:
        parts = []

        for part in path.split("/"):
            if part == "..":
                if parts:
                    parts.pop()
            elif part and part != ".":
                parts.append(part)

        # print(parts, "/" + "/".join(parts))
        return "/" + "/".join(parts)

s = Solution()

testcases = [["/./", "/"],
             ["/./", "/"],
             ["/../", "/"],
             ["/home/", "/home"],
             ["/home/././././././", "/home"],
             ["/home/////./././//", "/home"],
             ["/home/user/..", "/home"],
             ["/home/user/../user/../user/../", "/home"],
             ["/home/user/../user/../user/../user/", "/home/user"],
             ["/home/foo", "/home/foo"],
             ["/home//foo/", "/home/foo"],
             ["/home//foo//", "/home/foo"],
             ["/home///foo//", "/home/foo"],
             ["/home///foo///", "/home/foo"]]

for case, expected in testcases:
    assert s.simplifyPath(case) == expected
    assert s.simplifyPathLessIfs(case) == expected