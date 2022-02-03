from typing import List

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        left = dict()
        right = dict()

        for a in range(len(nums1)):
            for b in range(len(nums2)):
                left[(a,b)] = nums1[a] + nums2[b]

        for c in range(len(nums3)):
            for d in range(len(nums4)):
                right[(c,d)] = nums3[c] + nums4[d]

        result = 0
        for l in left:
            for r in right:
                # print(nums1[l[0]], nums2[l[1]], nums3[r[0]], nums4[r[1]],
                #       "==", left[l], "+", right[r], "==", left[l] + right[r])
                if left[l] + right[r] == 0:
                    result += 1

        # print(len(left), len(right), results)
        return result

    # very cleverly a counting problem
    # is there a way to compact the number of loops I'm doing? Or generalize for k sets of pairwise loops?
    # still not fast enough... seems like there's room for optimization
    def fourSumCount2(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ways2 = dict()
        ways3 = dict()
        ways4 = dict()

        for a in nums1:
            for b in nums2:
                if a+b not in ways2:
                    ways2[a+b] = 1
                else:
                    ways2[a+b] += 1

        for c in nums3:
            for w in ways2:
                if c+w not in ways3:
                    ways3[c+w] = ways2[w]
                else:
                    ways3[c+w] += ways2[w]

        for d in nums4:
            for w in ways3:
                if d+w not in ways4:
                    ways4[d+w] = ways3[w]
                else:
                    ways4[d+w] += ways3[w]

        if 0 in ways4:
            return ways4[0]
        return 0

    # can't escape O(n**2)
    # loosely based somewhere between my previous solution and this one
    # https://leetcode.com/problems/4sum-ii/discuss/93917/Easy-2-lines-O(N2)-Python
    def fourSumCount3(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ways2 = dict()
        result = 0

        for a in nums1:
            for b in nums2:
                if a+b not in ways2:
                    ways2[a+b] = 1
                else:
                    ways2[a+b] += 1

        for c in nums3:
            for d in nums4:
                if -c-d in ways2:
                    result += ways2[-c-d]

        return result

s = Solution()

# assert s.fourSumCount([1,2],[-2,-1],[-1,2],[0,2]) == 2
# assert s.fourSumCount2([1,2],[-2,-1],[-1,2],[0,2]) == 2
# assert s.fourSumCount([0],[0],[0],[0]) == 1
# assert s.fourSumCount2([0],[0],[0],[0]) == 1

l1 = [0] * 20
l2 = [0] * 100
# assert s.fourSumCount(l1, l1, l1, l1) == 160000 # too slow
# assert s.fourSumCount(l2, l2, l2, l2) == 100000000 # too slow
assert s.fourSumCount2(l1, l1, l1, l1) == 160000
assert s.fourSumCount3(l1, l1, l1, l1) == 160000
assert s.fourSumCount2(l2, l2, l2, l2) == 100000000
assert s.fourSumCount3(l2, l2, l2, l2) == 100000000