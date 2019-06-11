# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.helper(l1, l2, 0)

    def helper(self, l1, l2, carry = 0):
        # print(l1 and l1.val, l2 and l2.val, carry)
        if not l1 and not l2:
            if carry > 0:
                return ListNode(carry)
            else:
                return None
        elif not l1:
            update = (l2.val + carry) % 10
            carry = (l2.val + carry) // 10
            l2.val = update
            # print("l2", l2.val, carry)
            l2.next = self.helper(None, l2.next, carry)
            return l2
        elif not l2:
            update = (l1.val + carry) % 10
            carry = (l1.val + carry) // 10
            l1.val = update
            # print("l1", l1.val, carry)
            l1.next = self.helper(l1.next, None, carry)
            return l1
        value = (l1.val + l2.val + carry) % 10
        carry = (l1.val + l2.val + carry) // 10
        node = ListNode(value)
        node.next = self.helper(l1.next, l2.next, carry)

        return node

    def addTwoNumbersIterative(self, l1: ListNode, l2: ListNode) -> ListNode:
        # pretty much https://leetcode.com/problems/add-two-numbers/discuss/1016/Clear-python-code-straight-forward
        # really neat code. Wish I thought of something similar.
        head = ListNode(0)
        current = head
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next

            if l2:
                carry += l2.val
                l2 = l2.next

            current.next = ListNode(carry % 10)
            carry = carry // 10
            current = current.next

        return head.next