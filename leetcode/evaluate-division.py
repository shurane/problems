from typing import List

class Solution:
    # super longwinded solution... how to shorten this?
    # TODO union-find version
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        mapping = dict()
        count = 0
        for a, b in equations:
            if a not in mapping:
                mapping[a] = count
                count += 1
            if b not in mapping:
                mapping[b] = count
                count += 1
        invmapping = dict((v,k) for k,v in mapping.items())

        # system of equations
        soe = [[0.0 for __ in range(count)] for _ in range(count)]
        for i in range(count):
            soe[i][i] = 1.0

        for index, (a, b) in enumerate(equations):
            ai = mapping[a]
            bi = mapping[b]

            soe[ai][bi] = values[index]
            soe[bi][ai] = 1 / values[index]

        def solve(ai, bi, visited):
            if (ai, bi) in visited or ai == bi:
                return

            # print("solve()", "ratio", f"{invmapping[ai]}/{invmapping[bi]}", "visited", [[invmapping[top], invmapping[bottom]] for top, bottom in visited])
            aibi = soe[ai][bi]

            visited[(ai, bi)] = None
            visited[(bi, ai)] = None

            # check if symbol is a numerator of one fraction and denominator of another
            # i.e. a/b = 2, b/c = 3. 'b' is both a numerator and denominator, then a/c = 6
            for ci in range(count):
                if (ai,ci) not in visited and soe[bi][ci] != 0.0 and soe[bi][ci] != 1.0:
                    aici = soe[ai][bi] * soe[bi][ci]
                    soe[ai][ci] = aici
                    soe[ci][ai] = 1 / aici
                    solve(ai, ci, visited)
                if (bi,ci) not in visited and soe[ai][ci] != 0.0 and soe[ai][ci] != 1.0:
                    bici = soe[ai][ci] * soe[bi][ai]
                    soe[bi][ci] = bici
                    soe[ci][bi] = 1 / bici
                    solve(bi, ci, visited)

        # keys = list(mapping)
        # # https://stackoverflow.com/a/59123981/198348 for formatting a 2D matrix
        # print("before")
        # print("   " + " ".join([f"{k:>8}" for k in keys]))
        # print(*(f"{keys[j]} " + " ".join([f"{i:8.3f}" for i in row]) for j, row in enumerate(soe)), sep="\n")

        # second pass
        visited = dict()
        for a, b in equations:
            solve(mapping[a], mapping[b], visited)

        # # https://stackoverflow.com/a/59123981/198348 for formatting a 2D matrix
        # print("after")
        # print("   " + " ".join([f"{k:>8}" for k in keys]))
        # print(*(f"{keys[j]} " + " ".join([f"{i:8.3f}" for i in row]) for j, row in enumerate(soe)), sep="\n")

        answers = []
        for a, b in queries:
            if a not in mapping or b not in mapping:
                answers.append(-1.0)
                continue

            ai = mapping[a]
            bi = mapping[b]

            if soe[ai][bi] != 0.0:
                answers.append(soe[ai][bi])
            else:
                answers.append(-1.0)

        # print("answers", answers)
        return answers

s = Solution()

assert s.calcEquation([["a","b"]], [2.0], [["a","b"],["b","a"]]) == [2.0, 0.5]
assert s.calcEquation([["a","b"]], [2.0], [["a","a"],["b","b"]]) == [1.0, 1.0]
assert s.calcEquation([["a","b"], ["c", "d"]], [2.0, 3.0], [["a","d"]]) == [-1.0]
assert s.calcEquation([["a","b"], ["b", "c"], ["c", "d"]], [2.0, 5.0, 10.0], [["a","d"], ["d", "a"]]) == [100.0, 0.01]
assert s.calcEquation([["a","b"], ["b", "c"], ["c", "d"]], [2.0, 5.0, 10.0], [["b", "d"]]) == [50.0]

assert s.calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]) == [6.0, 0.5, -1.0, 1.0, -1.0]
assert s.calcEquation([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]) == [3.75000,0.40000,5.00000,0.20000]
assert s.calcEquation([["a","b"]], [0.5], [["a","b"],["b","a"],["a","c"],["x","y"]]) == [0.50000,2.00000,-1.00000,-1.00000]

values = s.calcEquation([["x1","x2"],["x2","x3"],["x1","x4"],["x2","x5"]],
                      [3.0,0.5,3.4,5.6],
                      [["x2","x4"],["x1","x5"],["x1","x3"],["x5","x5"],["x5","x1"],["x3","x4"],["x4","x3"],["x6","x6"],["x0","x0"]]) # should derive x3/x4 or x4/x3
assert [round(value, 5) for value in values] == [1.13333,16.80000,1.50000,1.00000,0.05952,2.26667,0.44118,-1.00000,-1.00000]