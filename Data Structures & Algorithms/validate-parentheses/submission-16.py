class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if char  in mapping:
                maped  = stack.pop() if stack else "#"
                if mapping[char] != maped:
                    return False
            else:
                stack.append(char)

        return not stack