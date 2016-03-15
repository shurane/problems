import sys

N, T = map(int, sys.stdin.readline().split())
widths = map(int, sys.stdin.readline().split())

for test in range(T):
    i, j = map(int, sys.stdin.readline().split())
    print min(widths[i:j+1])
