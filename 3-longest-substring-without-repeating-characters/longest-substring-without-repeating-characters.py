class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window
       
        start = 0
        charSet = set()
        max_length = 0

        for end in range(len(s)):
            
            while s[end] in charSet:
                charSet.remove(s[start])
                start+=1
            
            charSet.add(s[end])
            max_length = max (max_length,(end - start + 1))
        
        return max_length




"""
"abcabcbb"
 s
 e
set = (a)
"abcabcbb"
 s
  e
set = (a,b)
"abcabcbb"
 s
   e
set = (a,b,c)
"abcabcbb"
  s
    e
set = (b,c,a)
"abcabcbb"
   s
     e
set = (c,a,b)
"abcabcbb"
    s
      e
set = (a,b,c)
"abcabcbb"
      s
       e
set = (c,b)
"abcabcbb"
        s
        e
set = (b)
"""


