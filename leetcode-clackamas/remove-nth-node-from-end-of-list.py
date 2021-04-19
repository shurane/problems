from helpers import ListNode

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        current = dummy
        for i in range(n):
            current = current.next

        second = dummy

        while current.next != None:
            current = current.next
            second = second.next

        remove = second.next
        second.next = remove.next

        return dummy.next