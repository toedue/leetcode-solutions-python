class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.split()
        return (len(x[-1]))


        """The Python split() method is a built-in function that splits a string into a list of substrings based on a specified separator. By default, it uses any sequence of whitespace (spaces, tabs, newlines) as the delimiter and removes empty strings from the result. 
        
        symtax:
        string.split(separator, maxsplit)
"""