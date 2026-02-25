from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target_length = len(p)
        target = Counter(p)
        result = []
        left = 0

        if len(s) < target_length:
            return result

        current = s[:target_length]
        current_count = Counter(current)

        if target == current_count:
                result.append(left)

        for right in range(target_length, len(s)):
            # remove left character
            current_count[s[left]] -= 1

            if current_count[s[left]] == 0:
                del current_count[s[left]]

            # add new right character
            current_count[s[right]] += 1

            left += 1
            
            if target == current_count:
                result.append(left)


        return result
        