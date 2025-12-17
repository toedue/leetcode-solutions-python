class Solution:
    def maxPower(self, s: str) -> int:
        i = 0 
        maxx = 1
        for j in range(1,len(s)):
            if s[j-1] != s[j]:
                length = j - i
                maxx = max(maxx,length)
                i = j
        length = len(s)-i
        maxx = max(maxx,length)
        return maxx

                





"""
leetcode
i
 i
 j
  j
  i
   j

"""