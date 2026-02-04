class Solution:
    def compress(self, chars: List[str]) -> int:
        counter = 0
        left = 0
        right = 0
        n = len(chars)
        s = ""

        while (right < n and left < n):
            while (right < n and chars[right] == chars[left]):
                right += 1
                counter +=1

            if counter == 1:
                s += chars[left]
                left = right
                counter = 0
            else:
                s += chars[left]
                s += str(counter)
                left = right
                counter = 0

        for i in range(len(s)):
            chars[i] = s[i]
            
        return len(s)
