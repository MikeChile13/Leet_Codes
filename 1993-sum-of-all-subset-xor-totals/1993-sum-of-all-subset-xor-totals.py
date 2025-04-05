class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total_subsets = [0]
        for num in nums:
            n = len(total_subsets)
            for i in range(n):
                xor = total_subsets[i]
                total_subsets.append(xor^num)
        # print(total_subsets)
        return sum(total_subsets)

