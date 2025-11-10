class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = defaultdict(int)
        result = 0

        for char in s:
            count[char] += 1
            if count[char]%2 == 0:
                result += 2
        for cnt in count.values():
            if cnt %2 == 1:
                result +=1
                break
        return result




        #A palindrome is a word, number, or phrase that reads the same forward and backward.
        