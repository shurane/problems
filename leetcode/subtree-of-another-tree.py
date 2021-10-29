from typing import Optional
from helpers2 import TreeNode, create_tree

class Solution:
    def isSubtree(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        if isSame(a, b):
            return True
        elif not a:
            return False
        return self.isSubtree(a.left, b) \
            or self.isSubtree(a.right, b)

def isSame(a: Optional[TreeNode], b: Optional[TreeNode]):
    if not a and not b:
        return True
    elif not a or not b:
        return False
    return a.val == b.val and isSame(a.left, b.left) and isSame(a.right, b.right)

# TODO look at merkle tree implementation, can be done in O(S) + O(T) instead of O(S) * O(T)
# https://leetcode.com/problems/subtree-of-another-tree/discuss/102741/Python-Straightforward-with-Explanation-(O(ST)-and-O(S%2BT)-approaches)
# and a simpler solution via https://leetcode.com/problems/subtree-of-another-tree/discuss/1130997/Python-or-O(n)-or-super-easy-to-understand

s = Solution()

l1a = create_tree([1,1])
l1b = create_tree([1])

l2a = create_tree([1,2])
l2b = create_tree([1])

l3a = create_tree([1,2,1])
l3b = create_tree([1])

l4a = create_tree([3,4,5,1,None,2])
l4b = create_tree([3,1,2])

l5a = create_tree([3,4,5,1,2])
l5b = create_tree([4,1,2])

assert s.isSubtree(l1a, l1b) == True
assert s.isSubtree(l2a, l2b) == False
assert s.isSubtree(l3a, l3b) == True
assert s.isSubtree(l4a, l4b) == False
assert s.isSubtree(l5a, l5b) == True