class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        setv = set()
        setv.add(0)
        for num in nums:
            if num not in setv:
                count += 1
                setv.add(num)
        return count


