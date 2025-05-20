class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        expected_freq = n//4
        Freqs = Counter(s)
        window = Freqs #technically tracking what's outside the window.

        if max(Freqs.values()) == expected_freq:
            return 0

        left = 0
        min_window = float('inf')

        for right in range(n):
            window[s[right]] -= 1
            
            while left <= right and max(window.values()) <= expected_freq:

                min_window = min(min_window,right - left + 1)
                window[s[left]] += 1
                left += 1

        return min_window

