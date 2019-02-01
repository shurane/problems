import string

class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        mapping = dict(zip(string.ascii_lowercase, morse))

        transformations = set()

        for word in words:
            t = "".join([mapping[letter] for letter in word])
            transformations.add(t)
        
        return len(transformations)

    
s = Solution()

input1 = ["gin", "zen", "gig", "msg"]

assert s.uniqueMorseRepresentations(input1) == 2

# 5 minutes 36 seconds