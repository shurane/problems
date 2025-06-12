# with Owen from Exponent
# https://www.tryexponent.com/practice/prepare/balanced-tree

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_balanced(node) -> bool:

    balance, _ = helper(node)
    return balance

def helper(node) -> tuple[bool, int]:
    if not node:
        return (True, 0)

    lbalance, ldepth = helper(node.left)
    rbalance, rdepth = helper(node.right)

    if not lbalance or not rbalance or abs(ldepth - rdepth) > 1:
        return (False, -1)

    return (True, 1 + max(ldepth, rdepth))

"""
            A
        B       C
    D               E
"""

# debug your code below
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
print(is_balanced(root))