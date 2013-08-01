
def m(n):
    """
    m(0) is undefined
    """
    bowls = [1 for bowl in xrange(n)]
    index=0
    counter=0

    while True:
        counter +=1
        index = bowls_distribute(bowls,index)
        #print index, bowls
        if bowls_allone(bowls):
            break

    return counter

def bowls_distribute(bowls, index=0):
    current=index
    for bean in xrange(bowls[index]):
        current += 1
        current = current % len(bowls)
        bowls[index] -= 1
        bowls[current] +=1
    return current

def bowls_allone(bowls):
    for bowl in bowls:
        if bowl != 1:
            return False
    return True

print m(5)
print m(100)

last = 0
for i in range(0,11):
    k = 2**i+1
    current = m(k)
    print "m(%s)" % (k), "=", current, "increased by", current - last
    last = current
