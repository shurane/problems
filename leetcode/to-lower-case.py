import string

class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return "".join([l.lower() if l in string.ascii_uppercase else l for l in str])