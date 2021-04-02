class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f"ListNode({self.val})"

    def printAll(self):
        return ListNode.print(self)

    @classmethod
    def print(cls, node):
        if not node:
            return "None"

        s = f"ListNode({node.val}"
        c = node.next
        while c:
            s += f" -> {c.val}"
            c = c.next
        s += ")"
        return s

    @classmethod
    def fromList(cls, lst):
        if not lst:
            return None

        dummy = ListNode()
        current = dummy

        for elem in lst:
            current.next = ListNode(elem)
            current = current.next

        return dummy.next
