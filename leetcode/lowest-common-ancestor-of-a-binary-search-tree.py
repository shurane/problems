from helpers import TreeNode

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        ps = self.binarySearchPathIterative(root, p)
        qs = self.binarySearchPathIterative(root, q)

        if not ps or not qs:
            return None

        i = 0
        while i < len(ps) and i < len(qs) and ps[i] == qs[i]:
            i += 1

        return ps[i-1]


    def binarySearchPathRecursive(self, root, node):
        path = self.binarySearchPathRecursiveHelper(root, node)
        if None in path:
            return []
        else:
            return path

    def binarySearchPathRecursiveHelper(self, root, node):
        if root == None:
            return [None]
        elif node.val < root.val:
            return [root] + self.binarySearchPathRecursiveHelper(root.left, node)
        elif node.val == root.val:
            return [root]
        else:
            return [root] + self.binarySearchPathRecursiveHelper(root.right, node)

    def binarySearchPathIterative(self, root, node):
        path = []
        while root:
            path.append(root)

            if node.val < root.val:
                root = root.left
            elif node.val == root.val:
                break
            else:
                root = root.right

            if root == None:
                path = []

        return path

t = TreeNode(6)

t.left = TreeNode(2)
t.left.left = TreeNode(0)
t.left.right = TreeNode(4)
t.left.right.left = TreeNode(3)
t.left.right.right = TreeNode(5)

t.right = TreeNode(8)
t.right.left = TreeNode(7)
t.right.right = TreeNode(9)

s = Solution()

# print(s.binarySearchPath(t, TreeNode(6)))
# print(s.binarySearchPath(t, TreeNode(5)))
# print(s.binarySearchPath(t, TreeNode(11)))
print(s.lowestCommonAncestor(t, t.left, t.right))