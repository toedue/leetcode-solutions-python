from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freq = defaultdict(int)
        left = 0
        maxLength = 0

        for right in range(len(s)):

            freq[s[right]] += 1

            # recompute the real max frequency
            maxFreq = max(freq.values())

            # if window invalid, shrink it
            while (right - left + 1) - maxFreq > k:
                freq[s[left]] -= 1
                left += 1
                maxFreq = max(freq.values())

            maxLength = max(maxLength, right - left + 1)

        return maxLength