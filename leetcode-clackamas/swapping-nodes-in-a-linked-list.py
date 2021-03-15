# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        left = head
        leftPrev = dummy
        i = 1

        while i < k:
            leftPrev = left
            left = left.next
            i += 1

        temp = left
        tempPrev = None
        while temp:
            temp = temp.next
            i += 1

        size = i
        j = size - k
        if j > k:
            temp = left
            tempPrev = leftPrev
            i = k
        else:
            temp = dummy.next
            tempPrev = dummy
            i = 1

        while i < j:
            tempPrev = temp
            temp = temp.next
            i += 1

        if left == temp:
            return head

        tempPrev.next = left
        leftPrev.next = temp

        temp2 = left.next
        left.next = temp.next
        temp.next = temp2

        print(left.val, temp.val)
        return dummy.next

s = Solution()
# assert s.swapNodes(ListNode.fromList([1]), 1) == ListNode.fromList([1])
# assert s.swapNodes(ListNode.fromList([1, 2]), 1) == ListNode.fromList([2, 1])
# assert s.swapNodes(ListNode.fromList([1, 2]), 2) == ListNode.fromList([2, 1])
# assert s.swapNodes(ListNode.fromList([1,2,3,4,5]), 1) == ListNode.fromList([5,2,3,4,1])
# assert s.swapNodes(ListNode.fromList([1,2,3,4,5]), 2) == ListNode.fromList([1,4,3,2,5])
# assert s.swapNodes(ListNode.fromList([1,2,3,4,5]), 3) == ListNode.fromList([1,2,3,4,5])
# assert s.swapNodes(ListNode.fromList([1,2,3,4,5]), 4) == ListNode.fromList([1,4,3,2,5])
# assert s.swapNodes(ListNode.fromList([1,2,3,4,5]), 5) == ListNode.fromList([5,2,3,4,1])