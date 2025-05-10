class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        first_zero = 0
        second_zero = 0
        first_sum, second_sum = 0,0
        for num in nums1:
            first_sum += num
            first_zero += (num == 0)
        first_sum += first_zero

        for num in nums2:
            second_sum += num
            second_zero += (num == 0)
        second_sum += second_zero

        if (first_zero == 0 and second_sum > first_sum) or (second_zero == 0 and first_sum > second_sum):
            return -1
        return max(first_sum,second_sum)