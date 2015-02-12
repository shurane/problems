def multiples(n, upto=6):
    return [n * i for i in xrange(1, upto+1)]

for i in xrange(int(1e7)):
    l = [sorted(str(elem)) for elem in multiples(i)]
    # http://stackoverflow.com/a/3844948/198348
    if l.count(l[0]) == len(l):
        print multiples(i)
