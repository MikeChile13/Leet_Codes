class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        key1 = defaultdict(int)
        key2 = defaultdict(int)
        i,j = 0,0
        for i in range(len(nums1)):
            key1[nums1[i]] += 1
        for i in range(len(nums2)):
            key2[nums2[i]] += 1
        res = []
        for key in key1.keys():
            if key in key2:
                res.extend([key]* min(key1[key],key2[key]))
        return res
