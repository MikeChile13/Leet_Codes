class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        length = len(nums[0])
        vals = set()
        for num in nums:
            vals.add(int(num,2))
        for i in range(2**length):
            if i not in vals:
                res = bin(i)[2:]
                return '0' * (length-len(res)) + res
        return