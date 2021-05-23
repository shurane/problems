from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # https://leetcode.com/problems/n-queens/discuss/19810/Fast-short-and-easy-to-understand-python-solution-11-lines-76ms
        # for further solutions, see https://rosettacode.org/wiki/N-queens_problem#Python:_Simple_Backtracking_Solution

        results = []
        self.helper(n, [], [], [], results)
        boards = [["." * i + "Q" + "." * (n-i-1) for i in ans] for ans in results]

        # for i, board in enumerate(boards):
        #     # https://stackoverflow.com/a/59123981/198348 for formatting a 2D matrix
        #     print(f"board #{i}")
        #     print(*("".join([f"{i}" for i in row]) for row in board), sep="\n")
        #     print()

        return boards

    def helper(self, n, queens, diffs, sums, results):
        p = len(queens)
        if p == n:
            results.append(queens)
            return

        for q in range(n):
            # interesting way to check if a new queen position overlaps from any existing ones
            if q not in queens and p - q not in diffs and p + q not in sums:
                self.helper(n, queens + [q], diffs + [p - q], sums + [p + q], results)


s = Solution()
# assert s.solveNQueens(4) == [[".Q..","...Q","Q...","..Q."],
#                              ["..Q.","Q...","...Q",".Q.."]]
s.solveNQueens(5)