class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        length = len(nums)
        min_heap = nums
        heapq.heapify(min_heap)
        operations = 0
        while length >= 2:
            a,b = heapq.heappop(min_heap),heapq.heappop(min_heap)
            if a > b:
                a,b = b,a
            if a >= k:
                break
            heapq.heappush(min_heap,a*2+b)
            length-=1
            operations+=1
        return operations