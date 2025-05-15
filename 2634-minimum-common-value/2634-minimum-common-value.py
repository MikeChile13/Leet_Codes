class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        min_val_found = -1
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                min_val_found = nums1[i]
                break
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return min_val_found