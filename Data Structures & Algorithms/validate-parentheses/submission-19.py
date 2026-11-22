class Solution:
    def isValid(self, s: str) -> bool:
        signs = {')': '(', '}':'{', ']':'['}
        stack = []

        for char in s:
            if char in signs:
                this = stack.pop() if stack else '#'
                if this != signs[char]:
                    return  False
            else:    
                stack.append(char)

        return not stack