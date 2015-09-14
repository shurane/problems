import sys
import itertools

num = int(sys.stdin.readline())
toys = map(int, sys.stdin.readline().split())
count = 0

toys = sorted(toys)

print toys

while toys:
    toy = toys[0]
    count += 1
    matched = list(itertools.takewhile(lambda t: toy <= t <= toy + 4, toys))
    print "toy '{}' matched the following toys: '{}'".format(toy, matched)
    map(toys.remove, matched)

#print "minimum number of toys:", count
print count

# running time
# on N toys
#   - sorting the list is O(n log n)
#   - iterating through the list == linear... O(n)
#   - filter() step is linear, if it's scanning through the entire list
#     and only removing 1 element at a time, then it's being called N
#     times --> O(n^2)
#   - itertools.takewhile() only scans as many elements as matches the
#     predicate
# O(n log n) + O(n) == O(n log n)

# 17 minutes, 15 seconds
