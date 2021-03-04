# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA = 0
        lenB = 0

        current = headA
        while current:
            lenA += 1
            current = current.next

        current = headB
        while current:
            lenB += 1
            current = current.next

        followA = headA
        followB = headB
        if lenA < lenB:
            for i in range(lenB - lenA):
                followB = followB.next
        elif lenB < lenA:
            for i in range(lenA - lenB):
                followA = followA.next

        while followA != None:
            if followA == followB:
                return followA
            followA = followA.next
            followB = followB.next

        return None

