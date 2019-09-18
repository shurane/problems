# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = getLength(headA)
        lenB = getLength(headB)
        diff = abs(lenA - lenB)

        smaller, truncated = None, None
        if lenA < lenB:
            smaller = headA
            truncated = getNthElem(headB, diff)
        else:
            smaller = headB
            truncated = getNthElem(headA, diff)

        return findIntersection(smaller, truncated)


def getLength(lst):
    count = 0
    while lst:
        lst = lst.next
        count += 1
    return count

def getNthElem(lst, n):
    i = 0
    while lst:
        if i == n:
            return lst
        lst = lst.next
        i += 1

    return None

def findIntersection(lstA, lstB):
    """assumes lstA and lstB are the same length"""
    #this algo is based on an idea Rajib came up with. Pretty clever
    while lstA and lstB:
        if lstA == lstB:
            return lstA
        lstA = lstA.next
        lstB = lstB.next

    return None
