class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        largest = max(nums)
        n = len(nums)
        ks = 0
        left = 0

        subarrays = 0
        for right in range(n):
            if nums[right] == largest:
                ks += 1
            if ks == k:
                while ks == k:
                    if nums[left] == largest:
                        ks -= 1
                    left += 1
                    subarrays += n - right 
                # left += 1
        return subarrays


                