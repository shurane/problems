from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def fromListWithCycle(cls, lst: List, pos: int) -> 'ListNode':
        # can't reuse helpers2.ListNode() because its operations doesn't support LinkedLists with cycles
        # Note, existing methods (==, iter(), repr()) need to be modified to work with a ListNode with a cycle
        # see https://leetcode.com/problems/linked-list-cycle, https://leetcode.com/problems/linked-list-cycle-ii

        # consider somehow reusing ListNode.fromList()
        head = ListNode(None)
        cycleNode = None
        count = 0
        current = head
        for elem in lst:
            current.next = ListNode(elem)
            current = current.next

            if count == pos:
                cycleNode = current
            count += 1

        if cycleNode:
            current.next = cycleNode

        return head.next


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None

        slow = head
        fast = head.next
        while slow != fast:
            if fast.next == None or fast.next.next == None: return None
            slow = slow.next
            fast = fast.next.next

        # we're in a cycle
        current = slow.next
        count = 1
        while current != slow:
            current = current.next
            count += 1

        slow1 = head
        fast1 = head
        for i in range(count):
            fast1 = fast1.next

        while slow1 != fast1:
            slow1 = slow1.next
            fast1 = fast1.next

        return slow1

s = Solution()

l1 = ListNode.fromListWithCycle([3,2,0,-4], 1)
l2 = ListNode.fromListWithCycle([1,2], 0)
l3 = ListNode.fromListWithCycle([1,2,3,4,5,6], -1)
l4 = ListNode.fromListWithCycle([1], 0)
l5 = ListNode.fromListWithCycle([1], -1)

assert s.detectCycle(l1) == l1.next
assert s.detectCycle(l2) == l2
assert s.detectCycle(l3) == None
assert s.detectCycle(l4) == l4
assert s.detectCycle(l5) == None
