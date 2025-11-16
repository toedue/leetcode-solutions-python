class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"     # Base 7 of zero is simply "0"

        sign_mark = "-" if num < 0 else ""

        num = abs(num)

        answer = ""

        while num:
            digit = num % 7
            answer = str(digit) + answer
            num //= 7

        return sign_mark + answer



        