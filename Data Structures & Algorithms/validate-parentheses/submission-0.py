class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []

        if len(s) % 2 != 0:
            return False

        for char in  s:
            if char in mapping:
                maped = stack.pop() if stack else '#'

                if maped != mapping[char]:
                    return False
            else:
                stack.append(char)

        return not stack