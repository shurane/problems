from typing import List
import heapq

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diffs = []
        for a, b in costs:
            diffs.append((a - b, a, b))
        diffs.sort()

        k = len(costs) // 2
        total = 0

        for i in range(0, k):
            total += diffs[i][1]

        for i in range(k, len(costs)):
            total += diffs[i][2]

        return total

    def twoCitySchedCostShorter(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda person: person[0] - person[1])
        k = len(costs) // 2
        total = 0

        for i in range(0, k):
            total += costs[i][0]

        for i in range(k, len(costs)):
            total += costs[i][1]

        return total

    # def twoCitySchedCostHeap(self, costs: List[List[int]]) -> int:
        # acount = bcount = len(costs) // 2
        # A = []
        # B = []
        # visited =  [False] * len(costs)
        # for i, cost in enumerate(costs):
            # heapq.heappush(A, (cost[0], i))
            # heapq.heappush(B, (cost[1], i))

        # total = 0
        # while acount > 0 or bcount > 0:
            # print("total", total, "acount", acount, "bcount", bcount, "A", A, "B", B)
            # cost, i = None, None
            # if acount > 0 and A[0][0] < B[0][0]:
                # acount -= 1
                # cost, i = heapq.heappop(A)
            # elif bcount > 0 and B[0][0] < A[0][0]:
                # bcount -= 1
                # cost, i = heapq.heappop(B)
            # else:
                # if acount > 0:
                    # acount -= 1
                    # cost, i = heapq.heappop(A)
                # else:
                    # bcount -= 1
                    # cost, i = heapq.heappop(B)

            # visited[i] = True
            # total += cost

            # while A and visited[A[0][1]] == True: heapq.heappop(A)
            # while B and visited[B[0][1]] == True: heapq.heappop(B)

        # print("acount", acount, "bcount", bcount)

        # return total

s = Solution()

testcases = [[[[1,9],[1,9],[1,9],[1,9]], 20],
             [[[9,1],[9,1],[9,1],[9,1]], 20],
             [[[1,9],[1,9],[1,9],[9,1]], 12],
             [[[1,9],[1,9],[9,1],[9,1]], 4],
             [[[1,5],[9,1000]], 14],
             [[[10,20],[30,200],[400,50],[30,20]], 110],
             [[[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]], 1859],
             [[[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]], 3086]]

for costs, expected in testcases:
    assert s.twoCitySchedCost(costs) == expected
    assert s.twoCitySchedCostShorter(costs) == expected
    # print(s.twoCitySchedCostHeap(costs), expected)
    # assert s.twoCitySchedCostHeap(costs) == expected

