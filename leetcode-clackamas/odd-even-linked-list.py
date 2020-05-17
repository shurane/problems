from __future__ import annotations
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: ListNode = next

    def __repr__(self):
        s = f"ListNode({self.val}"

        current = self.next
        while current:
            s += f" > {current.val}"
            current = current.next

        return s + ")"

    def __eq__(self, other):
        c1, c2 = self, other

        while c1 and c2:
            if c1.val != c2.val:
                return False

            c1 = c1.next
            c2 = c2.next

        if not c1 and c2  or c1 and not c2:
            return False

        return True

    @classmethod
    def fromList(cls, lst: List[int]) -> ListNode:
        head = ListNode()
        current = head

        for value in lst:
            current.next = ListNode(value)
            current = current.next

        return head.next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        odd = ListNode(None)
        prev = ListNode(None)
        even = prev
        prev.next = head
        current = head
        oddEnd = odd
        count = 1

        while current:
            # print("prev:", prev, "current:", current, "odd:", odd)
            if count % 2 == 1:

                # remove node, keep the same prev, but reassign current
                temp = current
                current = current.next
                prev.next = current

                # add temp to end of odd list
                tempNext = oddEnd.next
                oddEnd.next = temp
                temp.next = tempNext

                # advance oddEnd
                oddEnd = oddEnd.next
            else:
                prev = current
                current = current.next

            count += 1

        oddEnd.next = even.next
        return odd.next


s = Solution()

# assert ListNode.fromList([]) == ListNode.fromList([])
# assert ListNode.fromList([]) != ListNode.fromList([1,2,3,4])
# assert ListNode.fromList([1,2,3,4,5]), ListNode.fromList([1,2,3,4,5])
# assert ListNode.fromList([1,2,3,4,5]) != ListNode.fromList([1,2,3,4])
# assert ListNode.fromList([1,2,3,4,5]) != ListNode.fromList([1,2,3,4,5,6])

l1 = ListNode.fromList([1,2,3,4,5])
l2 = ListNode.fromList([2,1,3,5,6,4,7])
l5 = ListNode.fromList([2])
l6 = ListNode.fromList([2,4,6,8,10,1,3,5,7,9])

assert s.oddEvenList(l1) == ListNode.fromList([1,3,5,2,4])
assert s.oddEvenList(l2) == ListNode.fromList([2,3,6,7,1,5,4])
assert s.oddEvenList(ListNode.fromList([])) == ListNode.fromList([])
assert s.oddEvenList(ListNode.fromList([1])) == ListNode.fromList([1])