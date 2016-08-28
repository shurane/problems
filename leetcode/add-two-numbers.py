# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __str__(self):
        result = ""
        current = self
        while current:
            if current.next:
                result += "{}->".format(current.val)
            else:
                result += "{}".format(current.val)
            current = current.next

        return result

    @classmethod
    def fromList(cls, lst):
        node = ListNode(None)
        prev = None
        current = node
        for elem in lst:
            current.val = elem
            current.next = ListNode(None)

            prev = current
            current = current.next

        # TODO is there a way that doesn't involve this last node?
        # get rid of the last node
        prev.next = None

        return node

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # programcreek helped a lot... http://www.programcreek.com/2012/12/add-two-numbers/
        
        d1 = l1
        d2 = l2
        l3 = ListNode(None)
        d3prev = None
        d3 = l3
        carry = 0
        while d1 != None or d2 != None:

            if d1 != None:
                carry += d1.val
                d1 = d1.next

            if d2 != None:
                carry += d2.val
                d2 = d2.next


            d3.next = ListNode(carry % 10)
            d3 = d3.next
            carry = carry / 10

        if carry != 0:
            next = ListNode(carry)
            d3.next = next

        # discard the first node
        return l3.next


s = Solution()
n1 = ListNode.fromList([2,4,3])
n2 = ListNode.fromList([5,6,4])

n3 = ListNode.fromList([2,4,5])
n4 = ListNode.fromList([2,4,3,4,2,7,8,6])

n5 = ListNode.fromList([1,8])
n6 = ListNode.fromList([0])

n7 = ListNode.fromList([9,8])
n8 = ListNode.fromList([1])

n9 = ListNode.fromList([9,9])
n10 = ListNode.fromList([1])

print s.addTwoNumbers(n1, n2)
print s.addTwoNumbers(n3, n2)

print "=================="

print s.addTwoNumbers(n4, n2)
print s.addTwoNumbers(n2, n4)
print s.addTwoNumbers(n5, n6)
print s.addTwoNumbers(n7, n8)
print s.addTwoNumbers(n9, n10)
