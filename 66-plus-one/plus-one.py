class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ""
        arr = []
        for i in digits:
            string += str(i)
        
        string = str(int(string) + 1)

        
        for i in string:
            arr.append(int(i))

        return arr

