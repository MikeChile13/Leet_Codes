class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        map_bracket = {
            '{':'}',
            '[':']',
            '(':')',
        }
        for i in range(len(s)):
            if s[i] in '{([':
                stack.append(s[i])
            elif stack and map_bracket[stack[-1]] == s[i]:
                stack.pop()
            else:
                return False
        return True if not stack else False