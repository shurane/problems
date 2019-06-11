from typing import List
from helpers2 import TreeNode

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0])

        n = len(nums)
        mid = (0 + n) // 2
        midnode = TreeNode(nums[mid])
        midnode.left  = self.sortedArrayToBST(nums[       :mid])
        midnode.right = self.sortedArrayToBST(nums[mid + 1:   ])
        
        return midnode
