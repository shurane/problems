from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # print("limit", limit, "people", people)
        people.sort()

        boats = 0
        l = 0
        r = len(people) - 1

        while l <= r:
            # print(people[l], people[r], limit)
            if l != r and people[l] + people[r] <= limit:
                boats += 1
                l += 1
                r -= 1
            else:
                boats += 1
                r -= 1

        return boats

    def numRescueBoatsSimpler(self, people: List[int], limit: int) -> int:
        people.sort()
        b, l, r = 0, 0, len(people) - 1

        while l <= r:
            if people[l] + people[r] <= limit: l += 1
            b += 1
            r -= 1

        return b

testcases = [[[1,2], 3, 1],
             [[3,2,2,1], 3, 3],
             [[3,5,3,4], 5, 4]]

s = Solution()

for people, limit, expected in testcases:
    assert s.numRescueBoats(people, limit) == expected
    assert s.numRescueBoatsSimpler(people, limit) == expected

