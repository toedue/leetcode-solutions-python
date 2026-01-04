class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        #
        up = low = 0
        for c in word:
            if c.isupper():
                up += 1
            else:
                low += 1
        return up==len(word) or low==len(word) or (up==1 and word[0].isupper())

        #return word.isupper() or word.islower() or word.istitle()