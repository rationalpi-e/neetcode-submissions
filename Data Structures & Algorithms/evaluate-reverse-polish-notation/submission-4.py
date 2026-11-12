import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        math_ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a,b : int(a/b)
        }

        stack = []
        
        for token in tokens:
            if token  in math_ops:
                a = stack.pop()
                b = stack.pop()
                res = math_ops[token](b, a)
                stack.append(res)
                
            else:
                stack.append(int(token))

        return stack[-1]
