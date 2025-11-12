class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = defaultdict(int)
        
        for char in s:
            d[char] += 1
        
        for key, value in d.items():
            if value == 1:
                return s.index(key)

        return -1
        