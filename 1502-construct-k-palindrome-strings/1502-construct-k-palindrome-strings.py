class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if n < k:
            return False
        if n == k:
            return True
        count = Counter(s)
        oddCount = 0
        for val in count.values():
            oddCount += val&1
        return oddCount <= k