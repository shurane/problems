import itertools

def skip_multiples(start=0,multiples=[]):
    num = start
    while True:
        factorless=True
        for multiple in multiples:
            if num % multiple == 0:
                factorless = False
        if factorless:
            yield num
        num += 1

def prime_sieve(upto=10000):
    numbers = [number for number in xrange(upto)]
    is_prime = [True for number in xrange(upto)]
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    for index, number in enumerate(numbers):
        if is_prime[index] == True:
            for multiple_index in xrange(index*2,upto,index):
                is_prime[multiple_index] = False

    return [number for number in numbers if is_prime[number]]

p = prime_sieve(upto=10000)

p = [prime for prime in p if len(str(prime)) == 4]

triplets = [ (prime, prime+3330, prime+3330+3330) for prime in p ]

for a,b,c in triplets:
    if a in p and b in p and c in p:
        if sorted(str(a)) == sorted(str(b)) and \
            sorted(str(b)) == sorted(str(c)):
            print(a,b,c)
