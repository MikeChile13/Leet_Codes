class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        valid = Counter('abc')
        window = Counter()
        n = len(s)
        validWindows = 0
        left = 0
        for right in range(n):
            window[s[right]] += 1
            validLeft = 0
            while window >= valid:
                validLeft += 1
                window[s[left]] -= 1
                left += 1
            validWindows += validLeft*(n - right)
        return validWindows