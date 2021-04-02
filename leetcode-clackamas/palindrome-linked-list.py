# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#     def __repr__(self):
#         return f"ListNode({self.val})"

from helpers import ListNode

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # O(n) with O(1) space, done by inverting first half of the linked list
        if not head or not head.next:
            return True
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # for even lists, move both nodes up one so slow is in the middle and fast becomes None
        # if fast:
        #     slow = slow.next
        #     fast = fast.next
        # print("head", ListNode.print(head))
        # print("half", ListNode.print(slow))
        # print(" end", ListNode.print(fast))

        # invert the first half of the linked list
        prev = None
        current = head
        while current != slow:
            switch = current.next
            current.next = prev
            prev = current
            current = switch

        right = current.next
        left = None
        # even length
        if fast:
            current.next = prev
            left = current
        # odd length, skip the middle element
        else:
            left = prev
        # print(left.printAll(), right.printAll())

        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True

    def isPalindromeList(self, head: ListNode) -> bool:
        lst = []
        c = head
        while c:
            lst.append(c.val)
            c = c.next
        return lst == lst[::-1]

s = Solution()

l1 = ListNode.fromList(list(range(1, 10)) + list(range(10, 0, -1))) #  odd list
l2 = ListNode.fromList(list(range(1, 11)) + list(range(10, 0, -1))) # even list

assert s.isPalindrome(None) == True
assert s.isPalindrome(ListNode.fromList([1])) == True
assert s.isPalindrome(ListNode.fromList([2,2])) == True
assert s.isPalindrome(ListNode.fromList([1,2])) == False
assert s.isPalindrome(ListNode.fromList([1,2,1])) == True
assert s.isPalindrome(ListNode.fromList([1,2,2,1])) == True
assert s.isPalindrome(ListNode.fromList(range(1, 20))) == False
assert s.isPalindrome(ListNode.fromList(range(1, 21))) == False
assert s.isPalindrome(l1) == True
assert s.isPalindrome(l2) == True

assert s.isPalindromeList(None) == True
assert s.isPalindromeList(ListNode.fromList([1])) == True
assert s.isPalindromeList(ListNode.fromList([2,2])) == True
assert s.isPalindromeList(ListNode.fromList([1,2])) == False
assert s.isPalindromeList(ListNode.fromList([1,2,1])) == True
assert s.isPalindromeList(ListNode.fromList([1,2,2,1])) == True
assert s.isPalindromeList(ListNode.fromList(range(1, 20))) == False
assert s.isPalindromeList(ListNode.fromList(range(1, 21))) == False
assert s.isPalindromeList(l1) == True
assert s.isPalindromeList(l2) == True