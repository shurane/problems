import random
import blessings
term = blessings.Terminal()

# this looks suspiciously a lot like the fisher yates algorithm
lst = range(30)

def colorized(lst, yellows=[]):
    result = "["
    delim = ", "
    for i in range(len(lst)):
        if i == len(lst) - 1:
            delim = ""

        v = "{: 3d}".format(lst[i])

        if i in yellows:
            result += term.yellow(v) + delim
        else:
            result +=             v  + delim

    result += "]"
    return result

def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp

def shuffle(lst):
    shuffled = lst[:]
    n = len(lst)
    i = 0
    while i < n:
        j = random.randrange(n-i)+i
        swap(lst, i, j)
        # print lst[:i], lst[i:]
        print colorized(lst, yellows=range(i))

        i += 1

shuffle(lst)
