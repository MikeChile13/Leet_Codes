class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        operations = 0
        while nums[0]<k:
            a,b = heapq.heappop(nums),heapq.heappop(nums)
            heapq.heappush(nums,a*2+b)
            operations+=1
        return operations