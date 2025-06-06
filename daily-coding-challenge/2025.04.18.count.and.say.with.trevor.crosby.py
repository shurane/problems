class Solution:
    def countAndSay(self, n: int) -> str:
        """
        countAndSay(1) =       1
        countAndSay(2) =       11
        countAndSay(3) =       21
        ... =                 1211
        =                    111221
                             312211
                            13112221
                           1113213211
                         31131211131221
                      13211311123113112211
                   11131221133112132113212221
               3113112221232112111312211312113211
         1321132132111213122112311311222113111221131221

        """

        # base case
        if n == 1:
            return str(1)

        s = self.countAndSay(n - 1)
        # 111221 -> 111 22 1 -> 31 12 11
        rle = ""

        i=0
        while i < len(s):
            j=i
            while j+1 < len(s) and s[i] == s[j+1]:
                j += 1

            count = j - i + 1

            rle += str(count) + s[i]

            i = j + 1

        print(n, rle, len(rle))

        return rle

s = Solution()
s.countAndSay(20)


