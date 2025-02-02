class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = []
        for string in s.split(' '):
            if string.isnumeric():
                nums.append(int(string))
        if len(nums) == 1:
            return True
        for i in range(1,len(nums)):
            if nums[i-1] >= nums[i]:
                return False
        return True