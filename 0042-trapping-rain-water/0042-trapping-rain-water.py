class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxleft,maxright = [0] * n,[0] * n
        for i in range(1,n):
            maxleft[i] = max(maxleft[i-1],height[i-1])
        for i in range(n-2,-1,-1):
            maxright[i] = max(maxright[i+1],height[i+1])
        sumv = 0
        for i in range(n):
            val = min(maxleft[i],maxright[i]) - height[i]
            sumv += val if val > 0 else 0
        return sumv