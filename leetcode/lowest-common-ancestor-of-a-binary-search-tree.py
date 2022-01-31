from helpers2 import TreeNode, create_tree

class Solution(object):
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ps = self.binarySearchPathIterative(root, p)
        qs = self.binarySearchPathIterative(root, q)

        if not ps or not qs:
            return None

        i = 0
        while i < len(ps) and i < len(qs) and ps[i] == qs[i]:
            i += 1

        return ps[i-1]

    def binarySearchPathRecursive(self, root: TreeNode, node: TreeNode):
        path = self.binarySearchPathRecursiveHelper(root, node)
        if None in path:
            return []
        else:
            return path

    def binarySearchPathRecursiveHelper(self, root: TreeNode, node: TreeNode):
        if root == None:
            return [None]
        elif node.val < root.val:
            return [root] + self.binarySearchPathRecursiveHelper(root.left, node)
        elif node.val == root.val:
            return [root]
        else:
            return [root] + self.binarySearchPathRecursiveHelper(root.right, node)

    def binarySearchPathIterative(self, root: TreeNode, node: TreeNode):
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

s = Solution()

t = create_tree([6,2,8,0,4,7,9,None,None,3,5])
# print(t.printLevels())

assert [node.val for node in s.binarySearchPathIterative(t, TreeNode(6))] == [6]
assert [node.val for node in s.binarySearchPathIterative(t, TreeNode(5))] == [6,2,4,5]
assert s.binarySearchPathIterative(t, TreeNode(11)) == []
assert s.lowestCommonAncestor(t, t.left, t.right) == t