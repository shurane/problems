from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        checked = set()

        for email in emails:
            first, domain = email.split("@")
            firstPrefix, _ = first.split("+", 1)
            firstPrefix = firstPrefix.replace(".","")

            cleanedEmail = f"{firstPrefix}@{domain}"
            checked.add(cleanedEmail)

        return len(checked)

# 8 minutes