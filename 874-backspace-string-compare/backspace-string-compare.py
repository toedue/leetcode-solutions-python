class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def remove_characters(x):
            stack = []
            for char in x:
                if char == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return stack

        return remove_characters(s) == remove_characters(t)
        
        