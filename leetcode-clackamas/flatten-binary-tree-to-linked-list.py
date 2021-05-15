from helpers import TreeNode

class Solution:
    def flatten(self, root: TreeNode) -> None:
        # https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/37010/Share-my-simple-NON-recursive-solution-O(1)-space-complexity!
        # iterating it as a linked list, but doing some moving to shift left to the right while preserving preorder traversal
        current = root
        while current:
            if  current.left:
                temp = current.left
                while temp.right:
                    temp = temp.right

                temp.right = current.right
                current.right = current.left
                current.left = None

            current = current.right

    def flattenWithStack(self, root: TreeNode) -> None:
        if not root: return
        elements = []
        q = [root]

        while q:
            n = q.pop()
            if not n: continue

            elements.append(n)
            q.append(n.right)
            q.append(n.left)

        for i in range(len(elements) - 1):
            # print(elements[i].val)
            elements[i].left = None
            elements[i].right = elements[i+1]

t1 = TreeNode.fromList([1,2,5,3,4,None,6])
t2 = TreeNode.fromListDirectional([1,2,3,4,5,6])
# print(t1.printAll())
# print(t2.printAll())

s = Solution()
assert t1 != t2
s.flatten(t1)
print(t1.printAll())
assert t1 == t2