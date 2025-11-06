class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        for i in range(len(s)):
            if s[i] in d1:
                d1[s[i]] += 1
            else:
                d1[s[i]] = 1
        for i in range(len(t)):
            if t[i] in d2:
                d2[t[i]] += 1
            else:
                d2[t[i]] = 1
        
        

        for char in d1:
            if d1.get(char, 0) != d2.get(char, 0):
                return False

            for char in d2:
                if d1.get(char, 0) != d2.get(char, 0):
                    return False

        return True

    