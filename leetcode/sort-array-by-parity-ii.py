class Solution:
    def sortArrayByParityII(self, A):
        def odds():
            for elem in A:
                if elem % 2 == 1:
                    yield elem
        def evens():
            for elem in A:
                if elem % 2 == 0:
                    yield elem

        # import itertools
        # return list(itertools.chain.from_iterable(zip(odds(), evens())))

        # alternatively:
        lst = []
        for a, b in zip(evens(), odds()):
            lst.append(a)
            lst.append(b)

        return lst


# [1,3,5,7,9,2,4,6,8,10]

s = Solution()
print(s.sortArrayByParityII([4,2,5,7]))
print(s.sortArrayByParityII([1,3,5,7,9,2,4,6,8,10]))