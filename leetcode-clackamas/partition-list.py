from helpers import ListNode
from colorama import init, Fore
init()

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:

        dummyHead = ListNode()
        dummyHead.next = head
        current = dummyHead

        # print("partition()")
        # print("before:", specialPrint(head, x))

        while current and current.next and current.next.val < x:
            current = current.next

        beforeGte = current
        gte = current.next

        lt = ListNode()
        ltTail = lt

        while current and current.next:
            if current.next.val < x:
                ltTail.next = current.next
                ltTail = ltTail.next
                current.next = current.next.next
            else:
                current = current.next

        # print(f"beforeGte: {beforeGte}, first node gte '{x}': {Fore.GREEN}{beforeGte.next}{Fore.RESET}"
        #       f", ltNodes after gte: {Fore.RED}{ListNode.printAll(lt.next)}{Fore.RESET}, ltTail: {ltTail}")

        if lt.next:
            beforeGte.next = lt.next
            ltTail.next = gte

        # print("answer:", specialPrint(dummyHead.next, x))

        return dummyHead.next

def specialPrint(head: ListNode, x: int) -> str:
    if not head:
        return str(None)

    s = f"{Fore.BLUE}x: {x}{Fore.RESET}, ListNode("

    current = head
    foundFirstGt = False
    while current:
        if current.val < x:
            s += f"{Fore.RED}{current.val}"
        elif current.val >= x and not foundFirstGt:
            s += f"{Fore.GREEN}{current.val}"
            foundFirstGt = True
        else:
            s += Fore.RESET + str(current.val)

        if current.next:
            s += " -> "

        current = current.next

    s += ")" + Fore.RESET

    return s


s = Solution()
# assert s.partition(ListNode.fromList([10,9,8,7,6,5,4,3,2,1]), 5) == ListNode.fromList([4,3,2,1,10,9,8,7,6,5])
# assert s.partition(ListNode.fromList([1,4,3,2,5,2]), 3) == ListNode.fromList([1,2,2,4,3,5])
# assert s.partition(ListNode.fromList([2,1]), 2) == ListNode.fromList([1,2])
assert s.partition(None, 2) == None
# assert s.partition(ListNode.fromList([1,2,3,4,5]), 6) == ListNode.fromList([1,2,3,4,5])
# assert s.partition(ListNode.fromList([1,2,3,4,5,6]), 6) == ListNode.fromList([1,2,3,4,5,6])
# assert s.partition(ListNode.fromList([7,8,9,10]), 6) == ListNode.fromList([7,8,9,10])
# assert s.partition(ListNode.fromList([6,7,8,9,10]), 6) == ListNode.fromList([6,7,8,9,10])