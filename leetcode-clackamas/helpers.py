from enum import Enum

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"

    def __eq__(self, other):
        a = self
        b = other
        while a and b:
            if a.val != b.val:
                return False
            a = a.next
            b = b.next

        if (not a and b) or (a and not b):
            return False

        return True

    def printAll(self):
        return ListNode.print(self)

    @classmethod
    def print(cls, node):
        if not node: return "ListNode(empty)"

        s = f"ListNode({node.val}"
        c = node.next
        while c:
            s += f" -> {c.val}"
            c = c.next
        s += ")"
        return s

    @classmethod
    def fromList(cls, lst):
        if not lst: return None

        dummy = ListNode()
        current = dummy

        for elem in lst:
            current.next = ListNode(elem)
            current = current.next

        return dummy.next

class D(Enum):
    # l = "Ⓛ"
    # r = "Ⓡ"
    l = "←"
    r = "→"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def inorder(self):
        q = [self]
        while q:
            n = q.pop(0)
            if not n: continue
            yield n.val
            q.append(n.left)
            q.append(n.right)

    def printAll(self):
        return TreeNode.print(self)

    @classmethod
    def print(cls, node, indent=2):
        if not node: return "TreeNode(empty)"

        s = f"TreeNode()\n{node.val}\n"
        stack = [
            (indent, node.right, D.r),
            (indent, node.left, D.l)
        ]
        while stack:
            i, n, d = stack.pop()

            if not n: continue

            v = str(n.val) if n else "None"
            s += " " * (i-indent) + "└" + " " * (indent - 1) + v + f" {d.value}" + "\n"

            stack.append((i + indent, n.right, D.r))
            stack.append((i + indent, n.left, D.l))

        return s.strip()

    @classmethod
    def fromList(cls, lst):
        if not lst: return None

        head = TreeNode(lst[0])
        tree = [head]

        for i in range(1, len(lst)):
            node = None
            if lst[i]: node = TreeNode(lst[i])
            tree.append(node)
            parent = (i-1) // 2

            if not node and not tree[parent]: continue

            if i % 2 == 1:
                tree[parent].left = node
            else:
                tree[parent].right = node

        return head

