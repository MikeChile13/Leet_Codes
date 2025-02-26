class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix_sum = 0
        largest_negative = 0
        largest_positive = 0
        result = 0
        
        for num in nums:
            prefix_sum += num
            if prefix_sum < 0:
                result = max(result,-prefix_sum + largest_positive)
                largest_negative = max(largest_negative,-prefix_sum)
            else:
                result = max(result,prefix_sum + largest_negative)
                largest_positive = max(largest_positive,prefix_sum)

        return result