from itertools import combinations, chain, permutations, product
import functools
import operator

ops = [operator.add, operator.sub, operator.div, operator.mul]

def opsmap(op):
    mapping = { operator.add : "+"
              , operator.sub : "-"
              , operator.div : "/"
              , operator.mul : "*"}
    if op in mapping:
        return mapping[op]
    else:
        return None

#from http://docs.python.org/2/library/itertools.html#recipes
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def generate_digits():
    start = 1
    while True:
        yield [start, start+1, start+2, start+3]
        start += 1

# permutation of 4 digits:  math.factorial(len(digits))
# 4 operators, choose 3:    len(combinations_with_replacement(ops,3))
# bracket placement:        len(powerset(combinations(range(len(digits)),2)))
# total?

def form_combinations2(digits,ops):
    digit_permutations = permutations(digits)
    ops_combinations = product(ops,repeat=len(digits)-1)
    bracket_combinations = powerset(combinations(range(len(digits)),2))
    count = 0
    for digitset in digit_permutations:
        for opset in ops_combinations:
            for bracketset in bracket_combinations:
                print(digitset,map(opsmap,opset),bracketset)
                count +=1
    print count

form_combinations2([1,2,3,4],ops)
