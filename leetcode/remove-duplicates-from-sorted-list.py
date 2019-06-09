# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        while current != None and current.next != None:
            successor = current.next
            
            if current.val == successor.val:
                current.next = successor.next
                successor = successor.next
                # don't advance current since there might be more duplicates
            else:
                # current and successor don't match, advance current
                current = successor
        return head
        

# test [1]
# test [1,1,2]
# test [1,1,2,3,3]
# test [1,1,1,1,1,1,1,1,1,1]
# test [1,1,1,1,1,1,1,1,1,1,2]
# test [0,1,1,1,1,1,1,1,1,1,1]