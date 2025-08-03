class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        max_heap = []
        for num in nums:
            heapq.heappush(max_heap,-int(num))
        while k-1:
            heapq.heappop(max_heap)
            k -= 1
        return str(-heapq.heappop(max_heap))