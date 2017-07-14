import sys

def maxsubarray(L):
    return L[0]


arrays = []
T = int(sys.stdin.readline())
for i in xrange(T):
    N = int(sys.stdin.readline())
    array = map(int, sys.stdin.readline().split())
    arrays.append(array)

