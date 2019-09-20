from helpers2 import ListNode

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        s = []
        oddCount = True

        slow = head
        fast = head.next

        while slow and fast:
            s.append(slow)

            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                oddCount = False

        # print("oddCount", oddCount)
        if oddCount:
            slow = slow.next

        # print(f"stack: {[node.val for node in s]}, middlePointer: {slow}")
        current = slow
        while current and s:
            top = s.pop()
            # print(current.val, top.val)
            if current.val != top.val:
                return False
            current = current.next
        return True

s = Solution()

t1 = ListNode.fromList([])
t2 = ListNode.fromList([1])
t3 = ListNode.fromList([1,2,3,3,2,1])
t4 = ListNode.fromList([1,2,3,2,1])
t5 = ListNode.fromList([1,2,3])
t6 = ListNode.fromList([1,2,3,4,2,1])

assert s.isPalindrome(t1) == True
assert s.isPalindrome(t2) == True
assert s.isPalindrome(t3) == True
assert s.isPalindrome(t4) == True
assert s.isPalindrome(t5) == False
assert s.isPalindrome(t6) == False