from typing import Optional
from helpers2 import ListNode

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0, head)
        p1 = dummy
        p2 = dummy and dummy.next
        curr = p2 and p2.next

        while p2 and curr:
            if p2.val == curr.val:
                while curr and curr.val == p2.val:
                    curr = curr.next
                p1.next = curr
                p2 = curr
                if curr: curr = curr.next
            else:
                p1 = p2
                p2 = curr
                curr = curr.next

        return dummy.next

    # https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/discuss/28336/Python-in-place-solution-with-dummy-head-node.
    def deleteDuplicatesSimpler(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = pre = ListNode(0, head)

        while head and head.next:
            if head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                pre = head
                head = head.next

        return dummy.next

s = Solution()

assert s.deleteDuplicates(ListNode.fromList([])) == ListNode.fromList([])
assert s.deleteDuplicatesSimpler(ListNode.fromList([])) == ListNode.fromList([])
assert s.deleteDuplicates(ListNode.fromList([1])) == ListNode.fromList([1])
assert s.deleteDuplicates(ListNode.fromList([1,2])) == ListNode.fromList([1,2])
assert s.deleteDuplicates(ListNode.fromList([1,2,3,4,5])) == ListNode.fromList([1,2,3,4,5])
assert s.deleteDuplicates(ListNode.fromList([1,2,3,4,5,5])) == ListNode.fromList([1,2,3,4])
assert s.deleteDuplicates(ListNode.fromList([1,1,2,3,4,5])) == ListNode.fromList([2,3,4,5])
assert s.deleteDuplicates(ListNode.fromList([1,2,3,3,4,5])) == ListNode.fromList([1,2,4,5])
assert s.deleteDuplicates(ListNode.fromList([1,1,1,2,2,3])) == ListNode.fromList([3])
assert s.deleteDuplicates(ListNode.fromList([1,1,2,2,3,3])) == ListNode.fromList([])
assert s.deleteDuplicatesSimpler(ListNode.fromList([1,1,2,2,3,3])) == ListNode.fromList([])
assert s.deleteDuplicates(ListNode.fromList([1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7,7])) == ListNode.fromList([1])
assert s.deleteDuplicatesSimpler(ListNode.fromList([1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7,7])) == ListNode.fromList([1])
