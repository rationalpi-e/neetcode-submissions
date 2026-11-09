class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        result = 0

        for _ in operations:
            if _ == 'C':
                stack.pop()
            elif _ == 'D':
                stack.append(stack[-1]  * 2)
            elif _ == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(_))

        for _ in stack:
            result += _

        return result