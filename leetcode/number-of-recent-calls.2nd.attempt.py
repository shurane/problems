import itertools

class RecentCounter:

    def __init__(self):
        self.past = []

    def ping1(self, t: int) -> int:
        # O(n) space and O(n) retrieval
        # might also be slow because of pop() shifting the array every time.
        self.past.append(t)
        while self.past and self.past[0] < t - 3000:
            self.past.pop(0)
        
        return len(self.past)
    
    def ping2(self, t: int) -> int:
        # store all the pings, but only retrieve the ones greater than t - 3000
        # still O(n) space and O(n) retrieval
        # probably correct, but hits "Time Limit Exceeded"
        self.past.append(t)
        
        count = 0
        for elem in reversed(self.past):
            if elem >= t - 3000:
                count += 1
            else:
                break
        return count 
    
    def ping3(self, t: int) -> int:
        # TODO implement LinkedList in tests.data.structures.py and use that in solution
        pass

# 5 minutes
# TODO would it be faster to use a linked list?