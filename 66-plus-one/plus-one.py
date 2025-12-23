class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str1 = ""
        for i in range(len(digits)):
            str1 += str(digits[i])
        integer = int(str1)
        increment = integer + 1
        str2 = str(increment)

        result = []

        for j in range(len(str2)):
            result.append(int(str2[j]))

        return result
