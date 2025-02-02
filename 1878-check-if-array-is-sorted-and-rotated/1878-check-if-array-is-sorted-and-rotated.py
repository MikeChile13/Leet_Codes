class Solution:
    def check(self, nums: List[int]) -> bool:
        current_index = 1
        length = len(nums)
        while current_index < length:
            if nums[current_index] < nums[current_index-1]:
                break
            current_index+=1
        # print(current_index)
        if current_index == length:
            return True
        while current_index < length-1:
            if nums[current_index] > nums[current_index+1]:
                return False
            current_index+=1
        # print(current_index)
        return nums[-1] <= nums[0]