from typing import List

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = dict()

        for p in paths:
            parts = p.split()
            path = parts[0]
            files = parts[1:]
            for f in files:
                left = f.find("(") + 1
                right = f.find(")")
                name = f[:left-1]
                content = f[left:right]
                if content not in d:
                    d[content] = []
                d[content].append("/".join([path,name]))
                # print(path, name, content)
        # for k, v in d.items():
        #     print(k, v)

        return [v for v in d.values() if len(v) > 1]

def compare_lists(lst1, lst2):
    return sorted(lst1) == sorted(lst2)

s = Solution()

l1 = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
l1_ans = [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
l2 = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]
l2_ans = [["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]]
l3 = ["root/a 1.txt(abcd) 2.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"]
# assert compare_lists(s.findDuplicate(l1), l1_ans)
# assert compare_lists(s.findDuplicate(l2), l2_ans)
assert compare_lists(s.findDuplicate(l3), [])