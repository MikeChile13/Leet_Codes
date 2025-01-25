class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        sorted = [(index,val) for val,index in enumerate(nums)]
        sorted.sort()
        mappings = {}
        mappings[sorted[0][1]] = 0
        buckets = [[0,0]]
        current_bucket = 0
        # print(sorted)
        for i in range(1,n):
            if sorted[i][0] - sorted[i-1][0] > limit:
                buckets.append([i,i])
            buckets[-1][1]=i
            current_bucket = len(buckets)-1
            mappings[sorted[i][1]] = current_bucket
        # print(buckets,mappings)
        for i in range(n):
            bucket = mappings[i]
            nums[i] = sorted[buckets[bucket][0]][0]
            buckets[bucket][0]+=1   
            # print(buckets)
        
        return nums
            
