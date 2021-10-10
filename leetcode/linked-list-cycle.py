from typing import Optional
from helpers2 import ListNode

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head.next if head else None

        while fast != None and slow != fast:
            slow = slow.next
            fast = fast.next.next if fast.next else None

        if fast == None:
            return False
        else: # slow == fast
            return True

# TODO look at linked-list-cycle-ii for cycle implementation