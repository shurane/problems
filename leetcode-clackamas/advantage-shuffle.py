from typing import List

class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        ## https://leetcode.com/problems/advantage-shuffle/discuss/149842/Python-Greedy-Solution-Using-Sort
        ## very creative, involves A with increasing order and B with decreasing order, and lining up the ends
        ## if an elem in A can't beat B, then find the biggest element in B to pair that 'loser' with
        ## it's kind of like "Tian Ji's Horse Race": https://leetcode.com/problems/advantage-shuffle/discuss/149932/Python-greedy-sol-with-detailed-comment-Chinese-story%3A-Tian-Ji's-Horse-race

        greater = dict()
        sa = sorted(A)
        sb = sorted(B, reverse=True)
        for b in sb:
            if sa[-1] > b:
                elem = sa.pop()
                if b not in greater:
                    greater[b] = []
                greater[b].append(elem)
        # print("gt", greater, "leftovers", sa)
        ## confusing one liner
        # results = [greater[b].pop() if b in greater and greater[b] else sa.pop() for b in B]
        results = []
        for b in B:
            # print(f"b: {b}, greater: {greater}, leftovers: {sa}")
            if b in greater and greater[b]:
                results.append(greater[b].pop())
            else:
                results.append(sa.pop())
        # print(results)
        return results

# def advantaged(A: List[int], B: List[int]):
#     return all( i > j for i, j in zip(A, B))
# assert advantaged([2,11,7,15], [1,10,4,11]) == True
# assert advantaged([2,7,11,15], [1,10,4,11]) == False

s = Solution()

# assert s.advantageCount([2,7,11,15], [1,10,4,11]) == [2, 11, 7, 15]
# assert s.advantageCount([2,0,4,1,2], [1,3,0,0,2]) == [2,4,1,2,0]
# assert s.advantageCount([12,24,8,32], [13,25,32,11]) == [24,32,8,12]
assert s.advantageCount([15,15,4,5,0,1,7,10,3,1,10,10,8,2,3],
                        [4,13,14,0,14,14,12,3,15,12,2,0,6,9,0])