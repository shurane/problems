from __future__ import annotations
from typing import Optional

class Node:
    n: int
    left: Optional[Node]
    right: Optional[Node]
    parent: Optional[Node]
    value: int

    def __init__(self, n: int, parent = None):
        self.n = n
        self.left = None
        self.right = None
        self.parent = parent
        self.value = 0


def fib_iterative_pointer(n: int):
    root = Node(n)
    current = root

    while current:
        print(current.n, "start", "left:", current.left is not None, "right:", current.right is not None)
        if current.n <= 1:
            current.value = 1
            current = current.parent
            continue

        if not current.left:
            current.left = Node(current.n - 1, current)
            current = current.left
            continue

        if not current.right:
            current.right = Node(current.n - 2, current)
            current = current.right
            continue

        current.value = current.left.value + current.right.value

        print(current.n, "  fin", "left:", current.left is not None, "right: ", current.right is not None, current.value)
        current = current.parent


    return root.value

def fib_iterative2(N):
    if N == 0 or N == 1:
        return 1
    a = 0
    b = 1
    for i in range(N):
        old_a = a
        a = b
        b = old_a + b
    return b

print(fib_iterative_pointer(7))
print(fib_iterative2(7))
