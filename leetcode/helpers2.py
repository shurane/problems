from typing import List, Generator

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
        if type(self) != type(other):
            return False
        return self.val == other.val

    def printLevels(self, level = 0):
        s = f"{' ' * (2*level)}{level}:{self}\n"

        if self.left:
            s += "l" + self.left.printLevels(level + 1)

        if self.right:
            s += "r" + self.right.printLevels(level + 1)

        return s

# TODO this should be part of class Tree
def create_tree(lst: List):
    if len(lst) == 0:
        return None

    q = [TreeNode(lst[0])]

    for i in range(1, len(lst)):
        value = lst[i]
        if value != None:
            node = TreeNode(value)
            q.append(node)

            parent = (i - 1) // 2
            if i % 2 == 1:
                q[parent].left = node
            else:
                q[parent].right = node
        else:
            q.append(None)

    return q[0]

# TODO this should be part of class Tree
def create_tree_recursive(lst: List, i: int = 0):
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

def height(self, root: TreeNode) -> int:
    if not root:
        return 0
    else:
        return 1 + max(self.height(root.left), self.height(root.right))

def inorder(node: TreeNode) -> Generator[TreeNode, None, None]:
    if not node:
        return

    if node.left:
        yield from inorder(node.left)

    yield node

    if node.right:
        yield from inorder(node.right)

def preorder(node: TreeNode) -> Generator[TreeNode, None, None]:
    if not node:
        return
    yield node
    if node.left:
        yield from preorder(node.left)
    if node.right:
        yield from preorder(node.right)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        s = f"{self.val}"
        c = self.next
        while c:
            s += f" -> {c.val}"
            c = c.next

        return s

    def __iter__(self):
        current = self
        while current:
            yield current
            current = current.next

    def __eq__(self, other):
        if not other:
            return False

        l = self
        r = other
        while l and r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next

        if l or r:
            return False

        return True

    @classmethod
    def fromList(cls, lst: List):
        head = ListNode(None)
        current = head
        for elem in lst:
            current.next = ListNode(elem)
            current = current.next

        return head.next

    @classmethod
    def fromArgs(cls, *args):
        return ListNode.fromList(args)

    @classmethod
    def reverseList(start, end):
        pass

## testing for tree methods
# for lst in [[1,2,3,4,5,6], [1,2,3,4,None,6]]:
#     print("working with this list:", lst)
#     iterative = create_tree(lst)
#     print("iterative\n", iterative.printLevels())

#     recursive = create_tree_recursive(lst)
#     print("recursive\n", recursive.printLevels())
t1_lst = [8,4,12,2,6,10,14,1,3,5,7,9,11,13,15]
assert [t.val for t in inorder(create_tree(t1_lst))] == [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

## testing for listnode methods
assert ListNode.fromList([1,2,3])       == ListNode.fromList([1,2,3])
assert ListNode.fromList([])            != ListNode.fromList([1,2,3])
assert ListNode.fromList([1,2,3])       != ListNode.fromList([])
assert ListNode.fromList([1,2,3])       != ListNode.fromList([1,2,3,4])
assert ListNode.fromList([1,2,3,4])     != ListNode.fromList([1,2,3])
assert ListNode.fromArgs(1,2,3)         == ListNode.fromList([1,2,3])

def compareListOfLists(first: List[List[str]], second: List[List[str]]) -> bool:
    if len(first) != len(second):
        return False

    # sort the inner and outer lists
    first  = sorted([sorted(lst) for lst in first])
    second = sorted([sorted(lst) for lst in second])

    for l, r in zip(first, second):
        if l != r:
            return False

    return True

assert compareListOfLists([], []) == True
assert compareListOfLists([["a"]], []) == False
assert compareListOfLists([["a"]], ["a"]) == True
assert compareListOfLists([["a", "b"], ["c"]], [["c"], ["b", "a"]]) == True
assert compareListOfLists([["a", "b"], ["c", "d"]], [["d", "c"], ["b", "a"]]) == True
assert compareListOfLists([["a", "b"], ["c"]], [["d"], ["b", "a"]]) == False
