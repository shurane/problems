from typing import List, Optional
import heapq
from helpers2 import ListNode

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = ListNode(0)
        pointer = result
        minheap = []

        for i, linkedlist in enumerate(lists):
            if linkedlist:
                heapq.heappush(minheap, (linkedlist.val, i))

        while minheap:
            val, i = heapq.heappop(minheap)
            pointer.next = ListNode(val)
            pointer = pointer.next

            if lists[i].next:
                lists[i] = lists[i].next
                heapq.heappush(minheap, (lists[i].val, i))

        return result.next

s = Solution()
assert s.mergeKLists([ListNode.fromList([1,2,3]),ListNode.fromList([4,5,6]),ListNode.fromList([7,8,9])]) == ListNode.fromList([1,2,3,4,5,6,7,8,9])
assert s.mergeKLists([ListNode.fromList([1,4,7]),ListNode.fromList([2,5,8]),ListNode.fromList([3,6,9])]) == ListNode.fromList([1,2,3,4,5,6,7,8,9])
assert s.mergeKLists([ListNode.fromList([1,4,5]),ListNode.fromList([1,3,4]),ListNode.fromList([2,6])]) == ListNode.fromList([1,1,2,3,4,4,5,6])
assert s.mergeKLists([]) == None
assert s.mergeKLists([ListNode.fromList([])]) == None
