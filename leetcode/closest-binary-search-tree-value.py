class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return f"TreeNode({self.val})"

    def __eq__(self, other):
        if other is None:
            return False
        return self.val == other.val

    def printLevels(self, level = 0):
        s = f"{' ' * (2*level)}{level}:{self}\n"

        if self.left:
            s += "l" + self.left.printLevels(level + 1)

        if self.right:
            s += "r" + self.right.printLevels(level + 1)

        return s

def create_tree(lst: 'List'):
    # passing through values twice. inefficient, but simple to write without recursion
    q = []
    for value in lst:
        if value != None:
            node = TreeNode(value)
            q.append(node)
        else:
            q.append(None)

    for i in range(len(q)):
        node = q[i]
        if i*2 + 1 < len(q):
            node.left = q[i*2 + 1]

        if i*2 + 2 < len(q):
            node.right = q[i*2 + 2]

    if len(q) == 0:
        return None
    return q[0]

def create_tree_recursive(lst: 'List', i=0):
    if not lst:
        return None

    node = TreeNode(lst[i])

    left = i * 2 + 1
    if left < len(lst) and lst[left] != None:
        node.left = create_tree_recursive(lst, left)

    right = i * 2 + 2
    if right < len(lst) and lst[right] != None:
        node.right = create_tree_recursive(lst, right)

    return node

## testing for tree methods
# for lst in [[1,2,3,4,5,6], [1,2,3,4,None,6]]:
#     print("working with this list:", lst)
#     iterative = create_tree(lst)
#     print("iterative\n", iterative.printLevels())

#     recursive = create_tree_recursive(lst)
#     print("recursive\n", recursive.printLevels())


class Solution:
    def ClosestBST(self, s: 'TreeNode', k: 'int') -> 'TreeNode':
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
# print(t1.printLevels())

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