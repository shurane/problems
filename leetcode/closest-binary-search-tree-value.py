from helpers2 import TreeNode, create_tree

class Solution:
    def ClosestBST(self, s: TreeNode, k: int) -> TreeNode:
        # print("closestBST", s, k)
        if s == None:
            return None

        if k == s.val:
            return s

        closest = s
        if k < s.val:
            #go left
            left = self.ClosestBST(s.left, k)

            if left and abs(k - left.val) < abs(k - closest.val):
                closest = left
        else:
            #go right
            right = self.ClosestBST(s.right, k)
            if right and abs(k - right.val) < abs(k - closest.val):
                closest = right

        return closest

s = Solution()
t1 = create_tree([3,1,4,None,2,None,6])
t2 = create_tree([3])
t3 = create_tree([3,1])
t4 = create_tree([3,None,4])

assert s.ClosestBST(t1, 0) == TreeNode(1)
assert s.ClosestBST(t1, 2) == TreeNode(2)
assert s.ClosestBST(t1, 7) == TreeNode(6)

assert s.ClosestBST(t2, 0) == TreeNode(3)
assert s.ClosestBST(t2, 3) == TreeNode(3)
assert s.ClosestBST(t2, 6) == TreeNode(3)

assert s.ClosestBST(t3, 0) == TreeNode(1)
assert s.ClosestBST(t3, 3) == TreeNode(3)
assert s.ClosestBST(t3, 6) == TreeNode(3)

assert s.ClosestBST(t4, 0) == TreeNode(3)
assert s.ClosestBST(t4, 3) == TreeNode(3)
assert s.ClosestBST(t4, 6) == TreeNode(4)

# leetcode premium
# 26 minutes... needs work. But good idea. What do the solutions look like?
# in case of a tie, is there a preference to less than or greater than k?
