from helpers import ListNode, TreeNode

class Solution:
    def sortedListToBST(self, head: ListNode, first=True) -> TreeNode:
        if not head:
            return None
        elif not head.next:
            return TreeNode(head.val)

        prev = None
        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None
        left = self.sortedListToBST(head, False)
        right = self.sortedListToBST(slow.next, False)

        root = TreeNode(slow.val)
        root.left = left
        root.right = right

        # if first: print(root.printAll())

        return root

s = Solution()

s.sortedListToBST(ListNode.fromList([-10,-3,0,5,9]))
