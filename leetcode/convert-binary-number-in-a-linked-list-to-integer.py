from helpers2 import ListNode

class Solution:
    def getDecimalValueViaDigits(self, head: ListNode) -> int:
        digits = []
        current = head
        value = 0

        while current:
            digits.append(current.val)
            current = current.next

        power = 0
        while digits:
            value += 2**power * digits.pop()
            power += 1

        return value

    def getDecimalValue(self, head: ListNode) -> int:
        # see https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/discuss/451815/JavaPython-3-Simulate-binary-operations.
        value = 0

        while head:
            value = (value << 1) | head.val
            head = head.next

        return value


s = Solution()

assert s.getDecimalValue(ListNode.fromArgs(0)) == 0
assert s.getDecimalValue(ListNode.fromArgs(1)) == 1
assert s.getDecimalValue(ListNode.fromArgs(0, 1)) == 1
assert s.getDecimalValue(ListNode.fromArgs(1, 0)) == 2
assert s.getDecimalValue(ListNode.fromArgs(1, 0, 1)) == 5
assert s.getDecimalValue(ListNode.fromArgs(1, 1, 1, 1)) == 15
assert s.getDecimalValue(ListNode.fromArgs(0, 0)) == 0
assert s.getDecimalValue(ListNode.fromArgs(1,0,0,1,0,0,1,1,1,0,0,0,0,0,0)) == 18880