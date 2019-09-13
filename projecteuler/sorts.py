import random

def qsort(lst):
    if len(lst) <= 1:
        return lst

    pivot = random.choice(lst)
    # print "qsort(pivot={})".format(pivot)
    lefts = filter(lambda v: v<pivot, lst)
    rights = filter(lambda v: v>=pivot, lst)
    return qsort(lefts) + qsort(rights)

def mergesort(lst):
    # print("mergesort(lst={})".format(lst))
    if len(lst) <= 1:
        return lst
    if len(lst) == 2:
        if lst[1] < lst[0]:
            return [lst[1], lst[0]]
        else:
            return lst

    mid = len(lst) / 2
    lefts = mergesort(lst[:mid])
    rights = mergesort(lst[mid:])

    return merge(lefts, rights)


def merge(lefts, rights):
    i = 0
    j = 0
    index = 0
    results = []
    while i < len(lefts) and j < len(rights):
        if lefts[i] < rights[j]:
            results.append(lefts[i])
            i += 1
        else:
            results.append(rights[j])
            j += 1
    if i < len(lefts):
        results.extend(lefts[i:])
    else:
        results.extend(rights[j:])

    return results

def insertionsort(lst):
    for i in xrange(len(lst)):
        for j in xrange(i, 0, -1):
            if lst[j-1] < lst[j]:
                break
            else:
                lst[j-1], lst[j] = lst[j], lst[j-1]
    return lst


random.seed(0)
rand_list = [random.randint(0,10000) for i in xrange(50)]
ones = [1 for i in xrange(10000)]
print rand_list
r1 = qsort(rand_list[:])
r2 = mergesort(rand_list[:])
r3 = insertionsort(rand_list[:])
print r1 == r2
print r1 == r3

r4 = qsort(ones[:])
r5 = mergesort(ones[:])
r6 = insertionsort(ones[:])

print r4 == r5
print r5 == r6
