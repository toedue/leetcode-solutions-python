class Solution:
    def compress(self, chars: List[str]) -> int:
        counter = 0
        left = 0
        right = 0
        n = len(chars)
        s = ""
        res = []

        while (right < n and left < n):
            while (right < n and chars[right] == chars[left]):
                right += 1
                counter +=1

            if counter == 1:
                res.append(chars[left])
                left = right
                counter = 0
            else:
                res.append(chars[left])
                res.append(str(counter))
                left = right
                counter = 0
                
        s = "".join(res)

        for i in range(len(s)):
            chars[i] = s[i]

        return len(s)
