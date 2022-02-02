from typing import List

class Solution:
    # TODO union-find version, see https://leetcode.com/problems/evaluate-division/discuss/270993/Python-BFS-and-UF(detailed-explanation)
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = dict()

        # DFS approach. I should also try BFS.
        def solveGraph(a, b):
            # a > b > c, builds link a > c
            for c in list(graph[b]):
                if c in graph[a]:
                    continue

                value = graph[a][b] * graph[b][c]
                graph[a][c] = value
                graph[c][a] = 1 / value
                solveGraph(a, c)

        for index, (a, b) in enumerate(equations):
            if a not in graph:
                graph[a] = dict()
            if b not in graph:
                graph[b] = dict()

            graph[a][b] = values[index]
            graph[b][a] = 1 / values[index]

        for a, b in equations:
            solveGraph(a, b)
            solveGraph(b, a)

        answers = []
        for a, b in queries:
            if a not in graph or b not in graph[a]:
                answers.append(-1.0)
            else:
                answers.append(graph[a][b])

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
                      [["x2","x4"],["x1","x5"],["x1","x3"],["x5","x5"],["x5","x1"],["x3","x4"],["x4","x3"],["x6","x6"],["x0","x0"]]) # should derive x3/x4 and x4/x3
assert [round(value, 5) for value in values] == [1.13333,16.80000,1.50000,1.00000,0.05952,2.26667,0.44118,-1.00000,-1.00000]