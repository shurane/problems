from __future__ import annotations
from typing import Sequence, Optional, Any, Generator

class TreeNode:
    def __init__(self, x: Any = None):
        self.val: Any = x
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

    def __repr__(self) -> str:
        return f"TreeNode({self.val})"

    def __eq__(self, other) -> bool:
        if other is None:
            return False
        if type(self) != type(other):
            return False
        return self.val == other.val

    def printLevels(self, level: int = 0) -> str:
        s = f"{' ' * (2*level)}{level}:{self}\n"

        if self.left:
            s += "l" + self.left.printLevels(level + 1)

        if self.right:
            s += "r" + self.right.printLevels(level + 1)

        return s

    def binarySearchInsert(self, x: Any) -> None:
        if x < self.val:
            if self.left:
                self.left.binarySearchInsert(x)
            else:
                self.left = TreeNode(x)
        else:
            if self.right:
                self.right.binarySearchInsert(x)
            else:
                self.right = TreeNode(x)

# TODO this should be part of class Tree
def create_tree(lst: Sequence[Any]) -> Optional[TreeNode]:
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
            q.append(TreeNode(None))

    return q[0]

# TODO this should be part of class Tree
def create_tree_recursive(lst: Sequence[Any], i: int = 0) -> Optional[TreeNode]:
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

def height(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    else:
        return 1 + max(self.height(root.left), self.height(root.right))

def inorder(node: Optional[TreeNode]) -> Generator[TreeNode, None, None]:
    if not node:
        return

    if node.left:
        yield from inorder(node.left)

    yield node

    if node.right:
        yield from inorder(node.right)

def preorder(node: Optional[TreeNode]) -> Generator[TreeNode, None, None]:
    if not node:
        return
    yield node
    if node.left:
        yield from preorder(node.left)
    if node.right:
        yield from preorder(node.right)

# TODO generate random tree from list
# TODO generate random balanced tree of height h
# TODO generate balanced BST from input
# TODO generate tree diagram

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x: Any, next: Optional[ListNode] =None):
        self.val: Any = x
        self.next: Optional[ListNode] =next

    def __repr__(self) -> str:
        return self.trail()

    def __iter__(self):
        current = self
        while current:
            yield current
            current = current.next

    def __eq__(self, other) -> bool:
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

    def __hash__(self):
        """ See https://stackoverflow.com/questions/2909106/whats-a-correct-and-good-way-to-implement-hash """
        return hash(self.val)

    def trail(self, k: Optional[int] = None) -> str:
        """
        Returns string trail of k nodes after self. If k is None, returns all nodes.
        """
        i = 0
        s = f"{self.val}"
        c = self.next
        while c:
            if k is not None and i >= k: break
            i += 1
            s += f" -> {c.val}"
            c = c.next
        return s

    @classmethod
    def fromList(cls, lst: Sequence[Any]):
        head = ListNode(None)
        current = head
        for elem in lst:
            current.next = ListNode(elem)
            current = current.next

        return head.next

    @classmethod
    def fromArgs(cls, *args: Any):
        return ListNode.fromList(args)

    @classmethod
    def reverseList(cls, start, end):
        # TODO
        pass

def compareListOfLists(first: Sequence[Sequence[Any]], second: Sequence[Sequence[Any]]) -> bool:
    if len(first) != len(second):
        return False

    # sort the inner and outer lists
    first  = sorted([sorted(lst) for lst in first])
    second = sorted([sorted(lst) for lst in second])

    for l, r in zip(first, second):
        if l != r:
            return False

    return True

if __name__ == "__main__":
    t1_lst = [8,4,12,2,6,10,14,1,3,5,7,9,11,13,15]
    assert [t.val for t in inorder(create_tree(t1_lst))] == [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    assert [t.val for t in inorder(create_tree_recursive(t1_lst))] == [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

    t2_lst = [8,4,12,2,6,10,14,1,None,5,None,9,None,13,None]
    assert [t.val for t in inorder(create_tree(t2_lst))] == [1,2,4,5,6,8,9,10,12,13,14]
    assert [t.val for t in inorder(create_tree_recursive(t2_lst))] == [1,2,4,5,6,8,9,10,12,13,14]

    ## testing for listnode methods
    assert ListNode.fromList([1,2,3])       == ListNode.fromList([1,2,3])
    assert ListNode.fromList([])            != ListNode.fromList([1,2,3])
    assert ListNode.fromList([1,2,3])       != ListNode.fromList([])
    assert ListNode.fromList([1,2,3])       != ListNode.fromList([1,2,3,4])
    assert ListNode.fromList([1,2,3,4])     != ListNode.fromList([1,2,3])
    assert ListNode.fromArgs(1,2,3)         == ListNode.fromList([1,2,3])

    assert compareListOfLists([], []) == True
    assert compareListOfLists([["a"]], []) == False
    assert compareListOfLists([["a"]], [["a"]]) == True
    assert compareListOfLists([["a", "b"], ["c"]], [["c"], ["b", "a"]]) == True
    assert compareListOfLists([["a", "b"], ["c", "d"]], [["d", "c"], ["b", "a"]]) == True
    assert compareListOfLists([["a", "b"], ["c"]], [["d"], ["b", "a"]]) == False

    trail = ListNode.fromList([1,2,3,4,5])
    assert repr(trail) == "1 -> 2 -> 3 -> 4 -> 5"
    if trail:
        assert trail.trail() == "1 -> 2 -> 3 -> 4 -> 5"
        assert trail.trail(0) == "1"
        assert trail.trail(1) == "1 -> 2"
        assert trail.trail(2) == "1 -> 2 -> 3"
        assert trail.trail(3) == "1 -> 2 -> 3 -> 4"
        assert trail.trail(4) == "1 -> 2 -> 3 -> 4 -> 5"
        assert trail.trail(5) == "1 -> 2 -> 3 -> 4 -> 5"
        assert trail.trail(100) == "1 -> 2 -> 3 -> 4 -> 5"
