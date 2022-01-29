from helpers import TreeNode

# see https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/ for tips

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # return self.lowestCommonAncestorPath(root, p, q)
        return self.lowestCommonAncestorRecursive(root, p, q)

    def lowestCommonAncestorRecursive(self, root, p, q):
        if root == None or root == p or root == q:
            return root
        else:
            left = self.lowestCommonAncestorRecursive(root.left, p, q)
            right = self.lowestCommonAncestorRecursive(root.right, p, q)

            if left and right:
                return root
            else:
                return left or right


    def lowestCommonAncestorPath(self, root, p, q):
        ps = self.pathToNode(root, p)
        qs = self.pathToNode(root, q)

        if not ps or not qs:
            return None

        i = 0
        while i < len(ps) and i < len(qs) and ps[i] == qs[i]:
            i += 1

        return ps[i-1]

    def pathToNode(self, root, node):
        if root == None:
            return []
        elif root == node:
            return [node]
        else:
            left = self.pathToNode(root.left, node)
            if left:
                return [root] + left

            right = self.pathToNode(root.right, node)
            if right:
                return [root] + right

            if not left and not right:
                return []

s = Solution()

t = TreeNode(3)

t.left = TreeNode(5)
t.left.left = TreeNode(6)
t.left.right = TreeNode(2)
t.left.right.left = TreeNode(7)
t.left.right.right = TreeNode(4)

t.right = TreeNode(1)
t.right.left = TreeNode(0)
t.right.right = TreeNode(8)

# print(s.subtreeContainsNode(t, t))
# print(s.subtreeContainsNode(t, t.left))
# print(s.subtreeContainsNode(t, t.left.right.right))
# print(s.subtreeContainsNode(t, TreeNode(11)))

# print(s.pathToNode(t, t.left.right.right))
# print(s.pathToNode(t, TreeNode(11)))

print(s.lowestCommonAncestor(t, t.left, t.right))
print(s.lowestCommonAncestor(t, t.left, t.left.right.right))
# print(s.lowestCommonAncestor(t, t.left, TreeNode(11))) # should be None, but not part of testcase

"""
tt = listToTree([37,-34,-48,None,-100,-100,48,None,None,None,None,-54,None,-71,-22,None,None,None,8])

                    37
           -34                    -48
    None        -100        -100        48
None   None  None   None  -54   None  -71   -22


"""