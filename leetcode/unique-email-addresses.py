class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        
        checked = set()
        
        for email in emails:
            first, domain = email.split("@")
            firstPrefix, firstSuffix = first.split("+", 1)
            firstPrefix = firstPrefix.replace(".","")
            
            cleanedEmail = f"{firstPrefix}@{domain}"
            checked.add(cleanedEmail)
            
        return len(checked)

# 8 minutes