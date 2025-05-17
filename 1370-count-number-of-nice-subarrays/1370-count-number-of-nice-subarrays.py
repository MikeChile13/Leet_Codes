class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        nice = 0
        n = len(nums)
        left = 0
        gap = 0
        for right in range(n):
            if nums[right] % 2:
                count += 1
            
            if count == k:
                gap = 0

                while count == k:
                    count -= nums[left] % 2
                    gap += 1
                    left += 1

            nice += gap
        return nice 
            