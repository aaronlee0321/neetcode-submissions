import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }
        sum = 0
        stack = []
        for token in tokens:            
            if token not in ops: #digits
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                func = ops[token]
                ans = int(func(num1, num2))
                stack.append(ans)
        
        return int(stack.pop())