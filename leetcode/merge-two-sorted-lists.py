# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        s = f"{self.val}"
        c = self.next
        while c:
            s += f" -> {c.val}"
            c = c.next
        
        return s

def fromList(lst):
    if not lst:
        return None

    head = ListNode(lst[0])
    c = head
    for i in range(1, len(lst)):
        c.next = ListNode(lst[i])
        c = c.next

    return head

class Solution:
    def mergeTwoListsRecursive(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1
    
        if l1.val < l2.val:
            c = ListNode(l1.val)
            c.next = self.mergeTwoListsRecursive(l1.next, l2)
            return c
        else:
            c = ListNode(l2.val)
            c.next = self.mergeTwoListsRecursive(l1, l2.next)
            return c

    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        head = current = ListNode(0)

        while l1 != None and l2 != None:
            if l1.val < l2.val:
                current.next = ListNode(l1.val)
                current = current.next
                l1 = l1.next
            else:
                current.next = ListNode(l2.val)
                current = current.next
                l2 = l2.next

        if l1:
            current.next = l1
        else:
            current.next = l2

        return head.next


l1 = fromList([1,3,5,7])
l2 = fromList([2,4,6,8])
l3 = fromList([1,2,3])
l4 = fromList([4,5,6])
l5 = fromList([4,5,6,7,8,9,10,11])

s = Solution()
print(s.mergeTwoLists(l1, l2))
print(s.mergeTwoLists(l3, l4))
print(s.mergeTwoLists(l4, l3))
print(s.mergeTwoLists(l3, l5))
print(s.mergeTwoLists(l3, None))
print(s.mergeTwoLists(None, l3))

# 16 minutes iterative, 5 minutes recursive, 5 minutes simpler iterative