from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target_length = len(p)
        target = Counter(p)
        result = []

        for i in range(len(s)):
            current = s[i: i + target_length]
            current_count = Counter(current)

            if target == current_count:
                result.append(i)


        return result
        