from typing import Optional
from helpers2 import ListNode

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p, c, n = None, head, head.next if head else None

        while n:
            farNext = n.next
            c.next = p
            n.next = c

            p = c
            c = n
            n = farNext

        return c

s = Solution()

assert s.reverseList(ListNode.fromList([])) == ListNode.fromList([])
assert s.reverseList(ListNode.fromList([1])) == ListNode.fromList([1])
assert s.reverseList(ListNode.fromList([1,2])) == ListNode.fromList([2,1])

l1 = ListNode.fromList([1,2,3,4,5])
# print(l1)
r1 = s.reverseList(l1)
# print(r1)
assert r1 == ListNode.fromList([5,4,3,2,1])