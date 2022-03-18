# from helpers2 import ListNode
from typing import Dict, Sequence, Any, Optional

"""slightly different LinkedList node with random pointer"""
class Node:
    def __init__(self, val, next: Optional['Node'] = None, random: Optional['Node'] = None):
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
    def __hash__(self):
        return hash(self.val)
    @classmethod
    def fromList(cls, lst: Sequence[Any]) -> Optional['Node']:
        head = Node(0)
        current = head
        for elem in lst:
            current.next = Node(elem)
            current = current.next
        return head.next

class Solution:
    # not possible in 1 pass, but possible in 2 passes with O(n) extra space or 3 passes with O(1) extra space
    def copyRandomList(self, head: 'Node') -> 'Node':
        lookup: Dict[Node, Node] = dict()
        copy = Node(0)

        l = head
        r = copy
        while l:
            r.next = Node(l.val)
            r = r.next
            lookup[l] = r
            l = l.next

        l = head
        r = copy.next
        while l and r:
            if l.random:
                r.random = lookup[l.random]

            l = l.next
            r = r.next

        return copy.next # type: ignore

    # https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43485/Clear-and-short-python-O(2n)-and-O(n)-solution
    def copyRandomListSimpler(self, head: 'Node') -> 'Node':
        dic = dict()
        m = n = head
        while m:
            dic[m] = Node(m.val)
            m = m.next
        while n:
            dic[n].next = dic.get(n.next)
            dic[n].random = dic.get(n.random)
            n = n.next
        return dic.get(head)

def compareEqualAndCopied(l: Node, r: Node):
    o, c = l, r
    while o and c:
        if id(o) == id(c): return False
        elif o.val != c.val: return False
        elif o.random is not None and c.random is not None:
            if id(o.random) == id(c.random): return False
            elif o.random.val != c.random.val: return False
        o, c = o.next, c.next
    return o is None and c is None

s = Solution()

testcases = [[[1,2],[0,0]],
             [[1],[None]],
             [[3,3,3],[None,0,None]],
             [[0,1,2,3,4,5,6,7,8,9],[9,0,1,2,3,4,5,6,7,8]]]

for order, random in testcases:
    lookup = dict()
    rlookup = dict()
    orig = Node.fromList(order)
    if not orig: continue

    for i, node in enumerate(orig):
        lookup[i] = node
        rlookup[node] = i

    for i, randomNext in enumerate(random):
        lookup[i].random = lookup.get(randomNext)

    copy = s.copyRandomList(orig)
    copy2 = s.copyRandomListSimpler(orig)

    assert compareEqualAndCopied(orig, orig) == False
    assert compareEqualAndCopied(copy, copy) == False
    assert compareEqualAndCopied(orig, copy) == True
    assert compareEqualAndCopied(orig, copy2) == True

    # print(" order", " ->".join([f"{elem.val:2}" for elem in orig]))
    # print("random", " ->".join([f"{rlookup[elem.random]:2}" if elem.random else " Ø" for elem in orig]))
