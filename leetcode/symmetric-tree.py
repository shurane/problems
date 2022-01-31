from helpers2 import TreeNode

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isSymmetricMirror(root)

    def isSymmetricIterative(self, root: TreeNode):
        queue = [root, "EOL"]
        level = []

        while queue:
            node = queue.pop(0)

            if node == "EOL":
                # compare elements of the same level
                for l, r in zip(level, reversed(level)):

                    lval = getattr(l, "val", None)
                    rval = getattr(r, "val", None)
                    if lval != rval:
                        return False

                level = []
                if len(queue) > 0:
                    queue.append("EOL")
            else:
                level.append(node)
                if node != None:
                    queue.append(node.left)
                    queue.append(node.right)
        return True

    def isSymmetricIterativeLeetcode(self, root: TreeNode):
        q = []
        q.append(root)
        q.append(root)

        while q:
            t1 = q.pop(0)
            t2 = q.pop(0)
            if t1 == None and t2 == None:
                continue
            if t1 == None or t2 == None:
                return False
            if t1.val != t2.val:
                return False
            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)

        return True

    def isSymmetricMirror(self, root: TreeNode):
        if root == None:
            return True
        else:
            return self.isMirror(root.left, root.right)

    def isMirror(self, l: TreeNode, r: TreeNode):
        if l == None and r == None:
            return True
        elif l == None or r == None:
            return False
        else:
            return l.val == r.val \
            and self.isMirror(l.right, r.left) \
            and self.isMirror(l.left, r.right)

    def isSymmetricRecursive(self, root: TreeNode):
        # in order traversal with a stack would be better than using a generator
        # see: https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/
        if root == None:
            return True

        left = self.in_order_traversal(root)
        right = self.reverse_in_order_traversal(root)

        while True:
            lval = None
            try:
                lval = next(left)
            except StopIteration:
                pass

            rval = None
            try:
                rval = next(right)
            except StopIteration:
                pass

            # print(lval, rval)
            if lval != rval:
                return False

            if lval == None and rval == None:
                break
        return True

    def in_order_traversal(self, root: TreeNode, level: int = 0):
        if root.left:
            lefts = self.in_order_traversal(root.left, level+1)
            while True:
                try:
                    yield next(lefts)
                except StopIteration:
                    break

        yield (root.val, level)

        if root.right:
            rights = self.in_order_traversal(root.right)
            while True:
                try:
                    yield next(rights)
                except StopIteration:
                    break


    def reverse_in_order_traversal(self, root: TreeNode, level: int = 0):
        if root.right:
            rights = self.reverse_in_order_traversal(root.right, level+1)
            while True:
                try:
                    yield next(rights)
                except StopIteration:
                    break

        yield (root.val, level)

        if root.left:
            lefts = self.reverse_in_order_traversal(root.left)
            while True:
                try:
                    yield next(lefts)
                except StopIteration:
                    break

s = Solution()

t1 = TreeNode(1)
t2 = TreeNode(1)
t2.left = TreeNode(2)
t2.right = TreeNode(2)

assert s.isSymmetric(t1) == True
assert s.isSymmetric(t2) == True

t2.left.right = TreeNode(3)
assert s.isSymmetric(t2) == False

t2.right.left = TreeNode(3)
assert s.isSymmetric(t2) == True