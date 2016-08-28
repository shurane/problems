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
        
        d1 = l1
        d2 = l2
        l3 = ListNode(None)
        d3prev = None
        d3 = l3
        carryOver = 0
        while d1 != None and d2 != None:
            temp = carryOver + d1.val + d2.val
            if temp >= 10:
                carryOver = temp / 10
                temp = temp % 10
            else:
                carryOver = 0

            d3.val = temp
            
            d1 = d1.next
            d2 = d2.next

            d3.next = ListNode(None)
            d3prev = d3
            d3 = d3.next


        if d1:
            while d1:
                d3.val = d1.val + carryOver

                if (d3.val >= 10):
                    carryOver = d3.val / 10
                    d3.val = d3.val % 10
                else:
                    carryOver = 0

                d1 = d1.next

                d3.next = ListNode(None)
                d3prev = d3
                d3 = d3.next
        elif d2:
            while d2:
                d3.val = d2.val + carryOver

                if (d3.val >= 10):
                    carryOver = d3.val / 10
                    d3.val = d3.val % 10
                else:
                    carryOver = 0

                d2 = d2.next

                d3.next = ListNode(None)
                d3prev = d3
                d3 = d3.next


        if carryOver != 0:
            d3.val = carryOver
            d3prev = d3
            d3 = d3.next

        d3prev.next = None

        return l3

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

# print s.addTwoNumbers(n1, n2)
# print s.addTwoNumbers(n3, n2)

# print "=================="

# print s.addTwoNumbers(n4, n2)
# print s.addTwoNumbers(n2, n4)
# print s.addTwoNumbers(n5, n6)
# print s.addTwoNumbers(n7, n8)
print s.addTwoNumbers(n9, n10)
