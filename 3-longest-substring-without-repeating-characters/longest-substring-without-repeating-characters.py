class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window
        left = 0
        set_ = set()
        current = 0
        best = 0

        for right in range(len(s)):
            if s[right] not in set_:
                set_.add(s[right])
                current = (right - left) + 1
            else:
                # remove characters from the left until duplicate is gone
                while s[right] in set_:
                    set_.remove(s[left])
                    left += 1
                set_.add(s[right])
                current = (right - left) + 1
            best = max (best, current)

        return best



       
        








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


