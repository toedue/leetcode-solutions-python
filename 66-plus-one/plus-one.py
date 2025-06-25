class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string_list = [str(digit) for digit in digits ]
        string = ''.join(string_list)
        number = int(string)
        number += 1
        list2 = [int(digit) for digit in str(number)] 
        return list2