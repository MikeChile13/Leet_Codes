class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = Counter(s)
        start = 0
        window = Counter()
        parts = []
        
        
        for i in range(len(s)):
            char = s[i]
            if char not in window:
                window[char] = freq[char]

            window[char] -= 1
            if window[char] == 0:
                del window[char]

            if len(window) == 0:
                parts.append(i - start + 1)
                start = i + 1

        return parts
            
                

