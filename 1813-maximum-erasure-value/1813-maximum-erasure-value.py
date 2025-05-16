class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        sumv = 0
        seen = set()
        max_unique_sum = 0
        left = 0
        for right in range(len(nums)):
            while nums[right] in seen:
                sumv -= nums[left]
                seen.remove(nums[left])
                left += 1

            seen.add(nums[right])
            sumv += nums[right]
            max_unique_sum = max(max_unique_sum, sumv)
        return max_unique_sum
