class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = []
        for i,num in enumerate(nums):
            res.append('1' if num[i] == '0' else '0')
        return ''.join(res)