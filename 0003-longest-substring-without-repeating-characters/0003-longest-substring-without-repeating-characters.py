class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = defaultdict(int)
        left = 0
        n = len(s)
        size = 0
        for right in range(n):
            visited[s[right]] += 1

            while visited[s[right]] > 1:
                visited[s[left]] -= 1
                left += 1
            size = max(size, right - left+1)
            
        return size
