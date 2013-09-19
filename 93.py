from itertools import combinations, chain, permutations, product, count
import operator
import IPython
from StringIO import StringIO

ops = [operator.add, operator.sub, operator.div, operator.mul]

def opsmap(op):
    mapping = { operator.add : "+"
              , operator.sub : "-"
              , operator.div : "/"
              , operator.mul : "*"}
    if op in mapping:
        return mapping[op]
    else:
        return "_"

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
# wait, brackets can't overlap. I can't have ((0,2),(1,3)) as brackets!
#   equivalent: (a `op` (b `op2` c) `op3` d)
#   incorrect, but it becomes a new set of brackets: ((0,3),(1,2))
#   since I'm throwing the results in a set(), repeats don't matter

def form_combinations2(digits,ops):
    digit_permutations = permutations(digits)
    ops_combinations = list(product(ops,repeat=len(digits)-1))
    bracket_combinations = list(powerset(combinations(range(len(digits)),2)))
    combo = 0
    for digitset in digit_permutations:
        for opset in ops_combinations:
            for bracketset in bracket_combinations:
                flattened = []
                for left, right in bracketset:
                    flattened.append((left,"left"))
                    flattened.append((right,"right"))
                flattened = sorted(flattened)

                equation = StringIO()
                print(flattened)
                while flattened and flattened[0][0] == 0:
                    elem = flattened.pop(0)
                    if elem[1] == "left":
                        equation.write("(")
                    else:
                        equation.write(")")

                equation.write(digitset[0])
                for index,op,digit in zip(count(),opset,digitset[1:]):
                    equation.write(opsmap(op))

                    while flattened and flattened[0][0] == index:
                        elem = flattened.pop(0)
                        if elem[1] == "left":
                            equation.write("(")
                        else:
                            equation.write(")")

                    equation.write(digit)

                if combo == 1700:
                    IPython.embed()

                equation.close()
                #print(digitset,map(opsmap,opset),bracketset)
                #print(combo,bracketset)
                combo +=1
    print combo

form_combinations2([1,2,3,4],ops)
