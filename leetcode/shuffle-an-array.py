from typing import List
from random import randrange

# problem discussed with Rodolfo and Rajib
# would be nice to check that for k runs, that the numbers are uniformly distributed
def generateRandomOrder(n: int) -> List[int]:
    result = [i*2 for i in range(1,n+1)]

    for i in range(n):
        j = randrange(i,n)

        temp = result[i]
        result[i] = result[j]
        result[j] = temp

    return result

# print(generateRandomOrder(10))
# print(generateRandomOrder(10))

class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        shuffled = list(self.nums)
        for i in range(self.n):
            rand_i = random.randrange(i, self.n)
            temp = shuffled[i]
            shuffled[i] = shuffled[rand_i]
            shuffled[rand_i] = temp

        return shuffled