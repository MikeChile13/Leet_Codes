class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # nums.sort()
        mapped = set(nums)
        max_count = -1
        for num in mapped:
            count = 0
            current = num
            while current <= 10**9 and current in mapped:
                count += 1
                current *= current
            if count > 1:
                max_count = max(max_count,count)
        return max_count