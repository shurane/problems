from helpers2 import ListNode
from typing import Dict

"""slightly different LinkedList node with random pointer"""
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
    def __iter__(self):
        current = self
        while current:
            yield current
            current = current.next
    def __repr__(self):
        s = f"{self.val}"
        c = self.next
        while c:
            s += f" -> {c.val}"
            c = c.next

        return s

class Solution:
    def copyRandomList(self, head: 'Node'):
        lookup: Dict[int, 'Node'] = dict()

        copy = Node(None, None, None)

        l = head
        r = copy
        while l:
            r.next = Node(l.val, None, None)
            r = r.next
            lookup[id(l)] = r
            l = l.next

        l = head
        r = copy.next
        while l:
            if l.random:
                r.random = lookup[id(l.random)]

            l = l.next
            r = r.next

        return copy.next

    # TODO
    # [ ] is there a way to do this without id() or getting the address of the node?
    #   - i.e. just marking the nodes from 1 to n?
    # [ ] is there a way to do this in a single pass?


s = Solution()

t1 = ListNode.fromArgs(1,2)
t1.random = t1.next
t1.next.random = t1.next

t2 = ListNode.fromArgs(1)
t2.random = None


print(t1)
print([elem.random.val for elem in t1])
r1 = s.copyRandomList(t1)
print(r1)
print([elem.random.val for elem in r1])

r2 = s.copyRandomList(t2)
print(r2)
print([elem.random.val if elem.random else None for elem in r2])