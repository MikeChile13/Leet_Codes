class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[0])
        max_area = 0
        for i in range(1,len(points)):
            max_area = max(points[i][0]-points[i-1][0],max_area)

        return max_area