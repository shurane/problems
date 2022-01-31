from unittest import TestCase
from typing import List
from helpers2 import TreeNode, create_tree

# https://stackoverflow.com/a/31832447/198348
tc = TestCase("__init__")

class Solution:
    def pathSumHelper(self, root: TreeNode, sum: int) -> List[List[int]]:
        # print(root, sum)
        if not root:
            return [[None]]
        elif self.isLeaf(root):
            if sum == root.val:
                return [[root.val]]
            else:
                return [[None]]
        else:
            left = self.pathSumHelper(root.left, sum - root.val)
            right = self.pathSumHelper(root.right, sum - root.val)
            solutions = []

            # print(root, "left", left)
            # print(root, "right", right)

            if left != [[None]]:
                for partial in left:
                    solutions.append([root.val] + partial)
            if right != [[None]]:
                for partial in right:
                    solutions.append([root.val] + partial)

            # print(root, "solutions", solutions)
            return solutions

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        elif self.isLeaf(root) and sum != root.val:
            return []
        else:
            return self.pathSumHelper(root, sum)

    def isLeaf(self, node: TreeNode) -> bool:
        return node != None and not node.left and not node.right

s = Solution()

t0 = create_tree([5,4])
# the input in the problem is set up differently than how create_tree() works
t1 = create_tree([5,4,8,11,None,13,4,7,2,None,None,None,None,5,1])
t2 = create_tree([1])
tc.assertCountEqual(s.pathSum(t0, 5), [])
tc.assertCountEqual(s.pathSum(t0, 9), [[5,4]])
tc.assertCountEqual(s.pathSum(t1, 22), [[5,4,11,2], [5,8,4,5]])
tc.assertCountEqual(s.pathSum(t1, 23), [])
tc.assertCountEqual(s.pathSum(t1, 1), [])
tc.assertCountEqual(s.pathSum(t2, 0), [])

# https://leetcode.com/problems/path-sum-ii/discuss/36829/Python-solutions-(Recursively-BFS%2Bqueue-DFS%2Bstack)
# has many interesting approaches
# recursively, BFS + queue, DFS + stack
# I think my solution is the recursive approach