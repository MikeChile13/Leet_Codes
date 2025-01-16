class Solution:
    def findXOR(self,nums):
        return reduce(lambda x,y: x^y,nums)
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1,n2 = len(nums1),len(nums2)
        if n1 % 2 == 0 and n2 %2 == 0:
            return 0
        elif n1 % 2 == 0:
            return self.findXOR(nums1)
        elif n2 % 2 == 0:
            return self.findXOR(nums2)
        else:
            return self.findXOR(nums1) ^ self.findXOR(nums2)