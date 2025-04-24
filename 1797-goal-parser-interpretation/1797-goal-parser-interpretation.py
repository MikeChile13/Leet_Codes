class Solution:
    def interpret(self, command: str) -> str:
        res = ''

        stack = []

        for char in command:
            if char == 'G':
                res += char
                continue
            
            if char == ')':
                res += 'o' if stack[-1] == '(' else 'al'
                while stack[-1] != '(':
                    stack.pop()
            
            stack.append(char)
            
        return res
            

