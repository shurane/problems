# Definition for a binary tree node.

# TODO generate random tree from list
# TODO generate random balanced tree

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insertBSTStyle(self, x):
        if self.val == None:
            self.val = x
        if x < self.val:
            insertBSTStyle(self.left, x)
        else:
            insertBSTStyle(self.right, x)

    def str_helper(self, side="", indent=0):
        prefix = indent * " " + side
        if self.val == None:
            return ""
        elif self.left == None and self.right == None:
            return prefix + "Leaf({})\n".format(self.val)
        else:
            s = prefix + "TreeNode({}):\n".format(self.val)
            if self.left != None:
                s += self.left.str_helper(side="L-", indent=indent+2)
            if self.right != None:
                s += self.right.str_helper(side="R-", indent=indent+2)
            return s

    def __str__(self):
        return self.str_helper()

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        else:
            return self.isSameTree(p.left, q.left) \
               and self.isSameTree(p.right, q.right)

    def isSameTreeIterative(self, p, q):
        pass


a = TreeNode(1)

b = TreeNode(1)
b.left = TreeNode(5)

c = TreeNode(1)
c.right = TreeNode(7)
c.right.left = TreeNode(3)

d = TreeNode(1)

e = TreeNode(1)
e.left = TreeNode(5)

f = TreeNode(1)
f.right = TreeNode(7)
f.right.left = TreeNode(3)

s = Solution()
assert s.isSameTree(a,d) == True
assert s.isSameTree(a,f) == False

print str(a)
print str(b)
print str(c)
