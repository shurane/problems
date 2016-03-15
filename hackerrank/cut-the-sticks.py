import sys

N = int(sys.stdin.readline())
sticks = map(int, sys.stdin.readline().split())

while sticks:
    print len(sticks)
    smallest = min(sticks)

    def cut(stick):
        new_stick = stick - smallest
        if new_stick < 0:
            return 0
        else:
            return new_stick

    sticks = filter(lambda x: x > 0, map(cut, sticks))
