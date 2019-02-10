class Solution:
    def diStringMatch(self, S: 'str') -> 'List[int]':
        # this solution is non working

        N = len(S)
        lst = list(range(N + 1))
        match = []

        # match = [None]
        # if S[0] == "I":
        #     match = [0]
        #     del lst[0]
        # else:
        #     match = [lst[-1]]
        #     del lst[-1]


        i = 0
        while i < N:
            j = i
            letter = S[i]
            while j < N and S[j] == letter:
                j += 1
            length = j - i
            print(f"S:{S}, i:{i}, j:{j} ==== lst:{lst}, match:{match}, letter:{letter}, length:{length})")
            
            if letter == "I":
                increasing = lst[len(lst) - length:]
                print("increasing", increasing)
                match.extend(increasing)
                del lst[len(lst) - length:]
                # match.append(lst[-1])
                # del lst[-1]
            else:
                decreasing = list(reversed(lst[:length + 1]))
                print("decreasing", decreasing)
                match.extend(decreasing)
                del lst[0:length + 1]
                # match.append(lst[0])
                # del lst[0]
            
            i += 1
        
        return match
    
    def diStringMatch2(self, S: 'str') -> 'List[int]':
        match = []
        lo = 0
        hi = len(S)
        for i in S:
            if i == "I":
                match.append(lo)
                lo += 1
            else:
                match.append(hi)
                hi -= 1
        match.append(lo)
        return match

s = Solution()

print(s.diStringMatch2("IIII"))
print(s.diStringMatch2("DDDD"))
print(s.diStringMatch2("IDID"))
print(s.diStringMatch2("DIDI"))
print(s.diStringMatch2("DDI"))

"""
thought process:
starts with I, then start with 0
starts with D, then start with N-1
if you see a run of Is, take the length of the run from the end.
    IIID -> 12340

if you see a run of Ds, take the length of the run from the beginning.
    IDDD -> 04321

IIII -> 01234
DDDD -> 43210

IDID -> 04132
DIDI -> 40312

31 minutes and counting
20 minutes more

after looking at the solution, I feel kind of dumb. https://leetcode.com/problems/di-string-match/solution/
I guess I have to take my loss and move on.
"""