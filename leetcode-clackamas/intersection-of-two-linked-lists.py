# Definition for singly-linked list.
# class ListNode: #     def __init__(self, x):
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

# based on solution page
class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        followA = headA
        followB = headB

        # how does this work?
        # oooh... it 'adds' them up by iterating through a+c+b and b+c+a
        # the length of a+c+b and b+c+a are the same. Interesting trick...

        # a + c
        # (     a      )    (  c   )
        # a1 -> a2 -> a3 -> c1 -> c2

        # b + c
        #       (  b   )    (  c   )
        #       b1 -> b2 -> c1 -> c2

        # a + c + b
        # (     a      )    (  c   )    (  b   )
        # a1 -> a2 -> a3 -> c1 -> c2 -> b1 -> b2

        # b + c + a
        # (  b   )    (  c   )    (     a      )
        # b1 -> b2 -> c1 -> c2 -> a1 -> a2 -> a3

        while followA != followB:
            if followA == None:
                followA = headB
            else:
                followA = followA.next

            if followB == None:
                followB = headA
            else:
                followB = followB.next

        return followA

