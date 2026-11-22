import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {'+': operator.add,
                "-": operator.sub,
                "*": operator.mul,
                "/": lambda a, b : int(a/b)
                }

        stack = []
        result = 0

        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()
                result = ops[token](b, a)
                stack.append(result)

        return stack[-1]