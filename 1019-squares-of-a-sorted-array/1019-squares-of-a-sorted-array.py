class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        min_heap = []
        heapq.heapify(min_heap)
        for num in nums:
            heapq.heappush(min_heap,num**2)
        res = []
        while min_heap:
            res.append(heapq.heappop(min_heap))
        return res