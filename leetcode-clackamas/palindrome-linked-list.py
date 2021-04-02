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
        prev = None

        while fast and fast.next:
            switch = slow
            slow = slow.next
            fast = fast.next.next

            switch.next = prev
            prev = switch

        right = slow.next
        # if even length, move left to equal the node slow
        if fast:
            slow.next = prev
            prev = slow

        while prev and right:
            if prev.val != right.val:
                return False
            prev = prev.next
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

# assert s.isPalindrome(None) == True
# assert s.isPalindrome(ListNode.fromList([1])) == True
# assert s.isPalindrome(ListNode.fromList([2,2])) == True
# assert s.isPalindrome(ListNode.fromList([1,2])) == False
assert s.isPalindrome(ListNode.fromList([1,2,1])) == True
assert s.isPalindrome(ListNode.fromList([1,2,2,1])) == True
assert s.isPalindrome(ListNode.fromList([1,2,3,2,1])) == True
assert s.isPalindrome(ListNode.fromList(range(1, 20))) == False
assert s.isPalindrome(ListNode.fromList(range(1, 21))) == False
# assert s.isPalindrome(l1) == True
# assert s.isPalindrome(l2) == True

assert s.isPalindromeList(None) == True
assert s.isPalindromeList(ListNode.fromList([1])) == True
assert s.isPalindromeList(ListNode.fromList([2,2])) == True
assert s.isPalindromeList(ListNode.fromList([1,2])) == False
assert s.isPalindromeList(ListNode.fromList([1,2,1])) == True
assert s.isPalindromeList(ListNode.fromList([1,2,2,1])) == True
assert s.isPalindromeList(ListNode.fromList([1,2,3,2,1])) == True
assert s.isPalindromeList(ListNode.fromList(range(1, 20))) == False
assert s.isPalindromeList(ListNode.fromList(range(1, 21))) == False
assert s.isPalindromeList(l1) == True
assert s.isPalindromeList(l2) == True