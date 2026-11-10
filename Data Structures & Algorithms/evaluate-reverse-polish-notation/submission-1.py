import  operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        math_actions = {
            '+' : operator.add,
            '-' : operator.sub,
            '*' : operator.mul,
            '/' : lambda a, b: int(a/b)
        }

        mylist = []
        

        for _ in tokens:
            if _ in math_actions:
                a = mylist.pop()
                b = mylist.pop()
                result = math_actions[_](b, a)
                mylist.append(result)
            else:
                mylist.append(int(_))

        return mylist[0]