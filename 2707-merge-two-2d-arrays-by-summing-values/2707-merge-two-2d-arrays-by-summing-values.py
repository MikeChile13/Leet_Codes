class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        id_mapping = defaultdict(int)
        max_id = 0
        for id,val in nums1:
            id_mapping[id] += val
            max_id = max(max_id,id)
        for id,val in nums2:
            id_mapping[id] += val
            max_id = max(max_id,id)
        res = []
        for i in range(1,max_id+1):
            if i in id_mapping:
                res.append([i,id_mapping[i]])
        return res
