from __future__ import annotations
from typing import Callable

class FreqStack:
    def __init__(self):
        self.freq = [[]]
        self.count = dict()

    def push(self, val: int) -> None:
        # print(val, self.freq, self.count)
        if val in self.count:
            self.count[val] += 1
        else:
            self.count[val] = 1

        if self.count[val] > len(self.freq):
            self.freq.append([])
        self.freq[self.count[val] - 1].append(val)

    def pop(self) -> int:
        val = self.freq[~0].pop()
        self.count[val] -= 1
        if not self.freq[~0]:
            self.freq.pop()
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

def push(val: int) -> Callable[[FreqStack], None]:
    return lambda stack: stack.push(val)

def pop(expected: int) -> Callable[[FreqStack], None]:
    def f(stack: FreqStack) -> None:
        retval = stack.pop()
        # print(f"retval: {retval}, expected: {expected}")
        assert retval == expected
    return f

testcases = [[push(5), push(7), push(5), push(7), push(4), push(5), pop(5), pop(7), pop(5), pop(4), pop(7), pop(5)],
             [push(4), push(0), push(9), push(3), push(4), push(2), pop(4), push(6), pop(6), push(1), pop(1), push(1), pop(1), push(4), pop(4), pop(2), pop(3), pop(9), pop(0), pop(4)],
            ]

for case in testcases:
    fstack = FreqStack()

    for op in case:
        op(fstack)

## alternative way by looking at "op" and "val"
# testcases = [[("push", 5), ("push", 7), ("push", 5), ("push", 7), ("push", 4), ("push", 5), ("pop", 5), ("pop", 7), ("pop", 5), ("pop", 4)]]

# for case in testcases:
#     fstack = FreqStack()

#     for op, val in case:
#         if op == "push":
#             fstack.push(val)
#         elif op == "pop":
#             retval = fstack.pop()
#             print(f"retval: {retval}, expected: {val}")
#             assert retval == val