# https://leetcode.com/problems/product-of-array-except-self/
from pprint import pprint

def product_sum(nums: list[int]) -> list[int]:
    n = len(nums)
    bag = dict()

    val = 1
    for i in range(n-1,-1,-1):
        val *= nums[i]
        bag[(i,n-1)] = val

    val = 1
    for j in range(0,n):
        val *= nums[j]
        bag[(0,j)] = val

    # pprint(bag)

    res = []
    res.append(bag[(1, n-1)])

    for i in range(1, n-1):
        res.append(bag[0,i-1]*bag[i+1,n-1])

    res.append(bag[0,n-2])

    # print("res:", res)

    return res

def product_sum2(nums: list[int]) -> list[int]:
    prefix = [1 for _ in nums]

    prefix[0] = nums[0]
    for i in range(1, len(nums)):
        prefix[i] = prefix[i-1] * nums[i]

    result = [1 for _ in nums]
    postfix = 1

    i = len(nums) - 1

    while i > 0:
        result[i] = prefix[i-1] * postfix
        postfix *= nums[i]
        i -= 1
    result[0] = postfix

    return result

l1, l1_expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [3628800,1814400,1209600,907200,725760,604800,518400,453600,403200,362880]
l2, l2_expected = [-10, 15, 7, 11, -3, 8], [-27720,18480,39600,25200,-92400,34650]
l3, l3_expected = [-1,1,0,-3,3], [0,0,9,0,0]

assert(product_sum(l1) == l1_expected)
assert(product_sum(l2) == l2_expected)
assert(product_sum(l3) == l3_expected)

assert(product_sum2(l1) == l1_expected)
assert(product_sum2(l2) == l2_expected)
assert(product_sum2(l3) == l3_expected)