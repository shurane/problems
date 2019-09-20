from helpers2 import ListNode

class Solution:
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
            carry = carry // 10

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

print(s.addTwoNumbers(n1, n2))
print(s.addTwoNumbers(n3, n2))

print("==================")

print(s.addTwoNumbers(n4, n2))
print(s.addTwoNumbers(n2, n4))
print(s.addTwoNumbers(n5, n6))
print(s.addTwoNumbers(n7, n8))
print(s.addTwoNumbers(n9, n10))
