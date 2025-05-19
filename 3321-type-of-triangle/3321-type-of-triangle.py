class Solution:
    def triangleType(self, nums: List[int]) -> str:
        vals = set(nums)
        def sums(a,b,c):
            if (a + b <= c) or (a + c <= b) or (b + c <= a) :
                return False
            else:
                return True
        if sums(nums[0],nums[1],nums[2]):
            if len(vals) == 1:
                return 'equilateral'
            elif len(vals) == 2:
                return 'isosceles'
            else:
                return 'scalene' 
        else:
            return 'none'