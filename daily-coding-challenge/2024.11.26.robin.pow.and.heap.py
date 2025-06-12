# n ** m , +-*/
# o(m)
# logm
#     res=n
# I.
#    m = 2**i
#    res -> **m
#     1. m 16 -> / 2
#     2. 8,  while ->7
#     3. recursion, 2**i-1 < x < 2**i
# II.
#    m /= 2 -> 1
#    res -> **m

#    m = 15
#    n**4 -> 15-8 = 7,
#    n**3 -> 7-4 = 3,
#    n**2 -> 3-2 = 1,
#    n**1
#     n**2
#     (((m/2)-1)/2-1) # division trick with mod
#     m%2 ... 1 or 0
#     (m//2)%2 ... 1 or 0

#     2**2+2+1

def pow(base: int, exponent: int):
    print(f"pow(base:{base}, exponent: {exponent})")
    if (exponent == 1):
        return base

    i = 1
    result = base

    while i*2 < exponent:
        result *= result
        i *= 2

    return result * pow(base, exponent - i)


# print(pow(2,31))

# https://leetcode.com/problems/merge-k-sorted-lists/

# i don't hear you

# how about now? I just refreshed
# https://meet.google.com/tfy-irsd-omd?authuser=1

"""
logn


 |          0
 |
 \/      1        3

      8    4    _     10


[ 1 2 3 4 5 6 (0/3.5/20) ] push(0) push(20) push(3.5)

"""

# https://github.com/python/cpython/blob/main/Lib/heapq.py
class Heap:
    def __init__(self):
        # 1-indexed
        self.container = [None]

    def heapup(self, index):
        parent = (index)//2
        if parent > 0 and  self.container[parent] > self.container[index]:
            self.container[parent], self.container[index] = self.container[index], self.container[parent]
            self.heapup(parent)

    def heapdown(self, index):
        left = 2 * index
        right = 2 * index + 1
        largest = index

        if left < len(self.container) and self.container[left] < self.container[largest]:
            largest = left
        if right < len(self.container) and self.container[right] < self.container[largest]:
            largest = right
        if largest != index:
            self.container[largest], self.container[index] = self.container[index], self.container[largest]
            self.heapdown(largest)

    def push(self, val):
        self.container.append(val)
        self.heapup(len(self.container)-1)

    def peek(self):
        return self.container[1] if len(self.container) > 1 else None

    def pop(self):
        if len(self.container) > 1:
            self.container[1], self.container[-1] = self.container[-1], self.container[1]
            item = self.container.pop()
            self.heapdown(1)
            return item
        return None

    def __len__(self):
        return len(self.container) - 1

import random
random.seed(0)
h = Heap()

for i in range(50):
    h.push(random.randrange(100))

print("removing some elements from heap")
for i in range(20):
    print(h.pop(), end=' ')
print()
print("container:", h.container)

while h:
    print(h.pop(), end=' ')
print()
