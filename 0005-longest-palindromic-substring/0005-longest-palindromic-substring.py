class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_palindrome = ''
        if len(s) < 2:
            return s
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                temp = s[i:j]
                if temp == temp[::-1] and len(temp) > len(max_palindrome):
                    max_palindrome = temp
        return max_palindrome
                    