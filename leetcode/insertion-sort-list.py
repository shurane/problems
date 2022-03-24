from typing import Optional
from helpers2 import ListNode

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)

        curr = head
        while curr:
            prev = curr
            curr = curr.next
            prev.next = None
            insert(dummy, prev)

        return dummy.next

def insert(head, node):
    while head.next and node.val > head.next.val:
        head = head.next

    temp = head.next
    head.next = node
    node.next = temp
    # head.next, node.next = node, head.next # one liner

s = Solution()

assert s.insertionSortList(ListNode.fromList([4,2,1,3])) == ListNode.fromList([1,2,3,4])
assert s.insertionSortList(ListNode.fromList([1,2,3,4])) == ListNode.fromList([1,2,3,4])
assert s.insertionSortList(ListNode.fromList([4,3,2,1])) == ListNode.fromList([1,2,3,4])
assert s.insertionSortList(ListNode.fromList([1,1,2,2,3,3,4,4])) == ListNode.fromList([1,1,2,2,3,3,4,4])
assert s.insertionSortList(ListNode.fromList([4,4,3,3,2,2,1,1])) == ListNode.fromList([1,1,2,2,3,3,4,4])
assert s.insertionSortList(ListNode.fromList([1,2,3,4,1,2,3,4])) == ListNode.fromList([1,1,2,2,3,3,4,4])
assert s.insertionSortList(ListNode.fromList([4,3,2,1,4,3,2,1])) == ListNode.fromList([1,1,2,2,3,3,4,4])
