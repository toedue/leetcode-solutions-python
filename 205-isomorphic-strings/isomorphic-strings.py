class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        smapt, tmaps = {}, {} 

        for i in range (len(s)):
            chr1, chr2 = s[i], t[i]
            if (chr1 in smapt and smapt[chr1]!= chr2) or (chr2 in tmaps and tmaps[chr2] != chr1):
                return False
            smapt[chr1] = chr2
            tmaps[chr2] = chr1
        return True