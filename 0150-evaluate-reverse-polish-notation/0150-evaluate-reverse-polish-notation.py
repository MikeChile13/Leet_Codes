class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = 0
        mapv = {'+':operator.add,
                '-':operator.sub,
                '*':operator.mul,
                '/':lambda x,y: int(x/y) }
        stack = []
        for i in range(len(tokens)):
            try:
                stack.append(int(tokens[i]))
            except:
                n1 = stack.pop()
                n2 = stack.pop()
                ans = mapv[tokens[i]](n2,n1)
                stack.append(ans)
        return stack[-1]