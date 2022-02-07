from typing import List, Optional
from helpers2 import TreeNode, create_tree

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(begin, end):
            if begin == end:
                return None
            elif begin + 1 == end:
                return TreeNode(nums[begin])

            index = value = -1

            # how to stop scanning a second time? Essentially doing 2*N iterations here
            # this reminds me of quick sort. We look for a pivot, then end up scanning the left and right sides again
            for i in range(begin, end):
                if nums[i] > value:
                    index = i
                    value = nums[i]

            t = TreeNode(nums[index])
            t.left = helper(begin, index)
            t.right = helper(index+1, end)

            return t

        return helper(0, len(nums))

s = Solution()
assert s.constructMaximumBinaryTree([3,2,1]) == create_tree([3,None,2,None,None,1])
assert s.constructMaximumBinaryTree([1,2,3]) == create_tree([3,2,None,1])
assert s.constructMaximumBinaryTree([3,2,1,6,0,5]) == create_tree([6,3,5,None,2,0,None,None,1])
