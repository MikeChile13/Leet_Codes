class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        vals = set(nums)
        if min(vals) < k:
            return -1
        vals.discard(k)
        return len(vals)