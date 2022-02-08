from typing import List, Optional
from helpers2 import TreeNode, create_tree

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # linear based on https://leetcode.com/problems/maximum-binary-tree/discuss/106146/C%2B%2B-O(N)-solution
        # same, but in python: https://leetcode.com/problems/maximum-binary-tree/discuss/258364/Python-O(n)-solution-with-explanation.
        # also related: https://leetcode.com/problems/maximum-binary-tree/discuss/106147/c-8-lines-on-log-n-map-plus-stack-with-binary-search
        # sentinel value https://leetcode.com/problems/maximum-binary-tree/discuss/106146/C++-O(N)-solution/108588
        stack = [TreeNode(2**32 - 1)]

        for num in nums:
            t = TreeNode(num)
            while stack[-1].val < num:
                t.left = stack[-1]
                stack.pop()
            stack[-1].right = t
            stack.append(t)

        return stack[1]

s = Solution()
assert s.constructMaximumBinaryTree([3,2,1]) == create_tree([3,None,2,None,None,1])
assert s.constructMaximumBinaryTree([1,2,3]) == create_tree([3,2,None,1])
assert s.constructMaximumBinaryTree([3,2,1,6,0,5]) == create_tree([6,3,5,None,2,0,None,None,1])
assert s.constructMaximumBinaryTree([3,1,2,6,0,5]) == create_tree([6,3,5,None,2,0,None,None,1])
assert s.constructMaximumBinaryTree([2,1,3,6,0,5]) == create_tree([6,3,5,2,None,0,None,None,1])
