class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ss =0
        tt= 0
        for i in range(len(s)):
            ss+= ord(s[i])
        
        for i in range(len(t)):
            tt+= ord(t[i])

        return chr(tt-ss)




        