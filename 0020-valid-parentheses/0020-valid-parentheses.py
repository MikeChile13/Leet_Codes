class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {'{':'}',
                 '[':']',
                 '(':')'}
        for char in s:
            if char in match:
                stack.append(char)
            else:
                if not stack or match[stack[-1]] != char:
                    return False
                stack.pop()
        return not stack