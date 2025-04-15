class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 3:
            return s
        new_s = sorted(s[:n//2])
        # print(new_s)
        if n % 2 :
            return ''.join(new_s + [s[n//2]] + new_s[::-1])
        # print(new_s)
        return  ''.join(new_s + new_s[::-1]) 