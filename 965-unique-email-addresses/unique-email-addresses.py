class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for email in emails:
            local,domain = email.split("@")
            if "+" in local:
                local = local[:local.index("+")]
            s.add(local.replace(".",'') + "@" + domain)

        return len(s)
        