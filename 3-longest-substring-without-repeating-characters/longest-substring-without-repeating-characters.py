class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window
        left = 0
        set_ = set()
        current_size = 0
        maxx_size = 0

        for right in range(len(s)):
            if s[right] not in set_:
                set_.add(s[right])
                current_size = (right - left) + 1
            else:
                while(s[right] in set_):
                    set_.remove(s[left])
                    left += 1
                set_.add(s[right])
                current_size = (right - left) + 1


            maxx_size = max(maxx_size, current_size)

        return maxx_size



       
        








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


