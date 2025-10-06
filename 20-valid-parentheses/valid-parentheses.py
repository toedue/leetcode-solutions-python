class Solution:
    def isValid(self, s: str) -> bool:
        dic = { "(":")","{":"}","[":"]"}
        stack = []

        for char in s:
            if char in dic:
                stack.append(char)
            else:
                if stack == [] or dic[stack.pop()] != char:
                    return False
        """ if the string was valid, every opening bracket had a matching closing one → the stack becomes empty """
        if stack == []:
            return True
        else:
            return False

