from itertools import count, takewhile

def generate_pentagonal():
    for n in count(start=1):
        yield  (n * (3 * n - 1)) / 2

p = generate_pentagonal()
numbers = takewhile(lambda number: number < 1e8, p)
numbers = list(numbers)
numbers_set = set(numbers)
satisfy_sum  = set()
satisfy_diff = set()

for index_i, i in enumerate(numbers):
    if index_i % 1000 == 0:
        print("Working on... {0}".format(index_i))
    for j in numbers[index_i:]:
        if i+j in numbers_set:
            satisfy_sum.add((i,j))
        if j-i in numbers_set:
            satisfy_diff.add((i,j))

results = satisfy_sum.intersection(satisfy_diff)

# this is dumb, how do I know D = |P_k - P-j| is minimized? I would need a math
# proof for that, wouldn't I? Oh well. Poor wording on behalf of Euler.
for a,b in results:
    print("a:{0}, b:{1}, a+b:{2}, b-a:{3}".format(a,b,a+b,b-a))
