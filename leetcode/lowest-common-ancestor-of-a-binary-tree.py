from helpers2 import TreeNode, create_tree

# see https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/ for tips

class Solution(object):
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # return self.lowestCommonAncestorPath(root, p, q)
        return self.lowestCommonAncestorRecursive(root, p, q)

    def lowestCommonAncestorRecursive(self, root: TreeNode, p: TreeNode, q: TreeNode):
        if root == None or root == p or root == q:
            return root
        else:
            left = self.lowestCommonAncestorRecursive(root.left, p, q)
            right = self.lowestCommonAncestorRecursive(root.right, p, q)

            if left and right:
                return root
            else:
                return left or right

    def lowestCommonAncestorPath(self, root: TreeNode, p: TreeNode, q: TreeNode):
        ps = self.pathToNode(root, p)
        qs = self.pathToNode(root, q)

        if not ps or not qs:
            return None

        i = 0
        while i < len(ps) and i < len(qs) and ps[i] == qs[i]:
            i += 1

        return ps[i-1]

    def pathToNode(self, root: TreeNode, node: TreeNode):
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

t = create_tree([3,5,1,6,2,0,8,None,None,7,4])
# print(t.printLevels())

assert [node.val for node in s.pathToNode(t, t.left.right.right)] == [3,5,2,4]
assert s.pathToNode(t, TreeNode(11)) == []

assert s.lowestCommonAncestor(t, t.left, t.right) == t
assert s.lowestCommonAncestor(t, t.left, t.left.right.right) == t.left
# print(s.lowestCommonAncestor(t, t.left, TreeNode(11))) # should be None, but not part of testcase

"""
tt = create_tree([37,-34,-48,None,-100,-100,48,None,None,None,None,-54,None,-71,-22,None,None,None,8])

                    37
           -34                    -48
    None        -100        -100        48
None   None  None   None  -54   None  -71   -22
"""