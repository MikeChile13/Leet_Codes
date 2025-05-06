class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        n = len(height)
        right = n-1

        max_area = 0
        while right > left:
            max_area = max(max_area,min(height[right],height[left]) *(right - left))

            if height[right] <= height[left]:
                right -= 1
            else:
                left += 1
            # print(left,right)
        return max_area