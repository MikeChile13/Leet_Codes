class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_score = 0
        for i in range(n):
            for j in range(1,n):
                for k in range(2,n):
                    if i < j < k:
                        max_score = max(max_score,( nums[i] - nums[j] ) * nums[k])
        return max_score
