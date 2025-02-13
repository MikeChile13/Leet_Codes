class Solution:
    def halveArray(self, nums: List[int]) -> int:
        sumv= sum(nums)
        half = sumv/2
        ops = 0
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        while half > 0:
            maxv = -heapq.heappop(max_heap)
            # print(maxv)
            maxv /=2
            half -=maxv
            ops+=1
            heapq.heappush(max_heap,-maxv)
        # print(ops)
        return ops

