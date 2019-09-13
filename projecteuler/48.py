

def lastNDigits(number, N):
    digits = []
    while N > 0:
        digits.append(int(number % 10))
        number = number / 10
        N -= 1

    # I mean, this is straightforward, but reference just in case.
    # http://stackoverflow.com/a/490020/198348
    return int("".join(map(str,reversed(digits))))

total = 0
for number in xrange(1,1000+1):
    num = lastNDigits(number ** number,10)
    #print(number,num)
    total += num

print(lastNDigits(total,10))
