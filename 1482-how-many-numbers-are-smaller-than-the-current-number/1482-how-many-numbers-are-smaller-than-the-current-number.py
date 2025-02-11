class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        map = {}
        res = []
        for i,number in enumerate(sorted(nums)):
            if number not in map:
                map[number] = i
        for num in nums:
            res.append(map[num])
        return res