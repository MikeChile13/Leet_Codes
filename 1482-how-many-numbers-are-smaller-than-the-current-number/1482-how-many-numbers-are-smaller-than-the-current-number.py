class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        vals = sorted(nums)
        res = []
        mapping = {}

        for i in range(len(nums)):
            if vals[i] not in mapping:
                mapping[vals[i]] = i

        for i in range(len(nums)):
            res.append(mapping[nums[i]])

        return res