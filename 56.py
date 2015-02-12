
def digits(number):
    d = []
    while number > 10:
        d.append(number % 10)
        number /= 10
    d.append(number)
    return list(reversed(d))

maxdigitsum = 0
max_ab = ()
a = 0
b = 0
while a < 100:
    b = 0
    while b < 100:
        number = a ** b
        #print a, b, number
        sdn = sum(digits(number))
        if sdn > maxdigitsum:
            maxdigitsum = sdn
            max_ab = (a, b)
        b += 1
    a += 1

print max_ab, maxdigitsum
