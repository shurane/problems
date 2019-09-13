# find prime numbers under 100

primes = "2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97".split()
primes = [int(x) for x in primes]

primes = [2,3,5]

max = 1e8
answers = set()
def generate_hammond(i,c):
    c = c * primes[i]
    if len(answers) % 10000 == 0:
        print("#%s generate_hammond(%s,%s)" % (len(answers),i,c))
    if c < max:
        answers.add(c)
    else:
        return
    for number in range(i,len(primes)):
        generate_hammond(number, c)

for xy in range(0,len(primes)):
    generate_hammond(xy,1)
print(len(answers))
