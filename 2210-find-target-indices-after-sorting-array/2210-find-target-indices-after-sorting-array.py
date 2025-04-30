class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res = []

        for idx,num in enumerate(sorted(nums)):
            if num == target:
                res.append(idx)

        return res