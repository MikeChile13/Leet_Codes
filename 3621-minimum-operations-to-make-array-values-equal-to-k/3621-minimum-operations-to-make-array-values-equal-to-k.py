class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(set(nums), reverse= True)
        print(nums)
        count = 0
        for num in nums:
            if num > k:
                count += 1
            elif num < k:
                count = -1
                break
            else:
                continue
        return count if count > -1 else -1