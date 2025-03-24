class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        point_map = [0]*102
        points = 0

        for start,end in nums:
            point_map[start] += 1
            point_map[end + 1] -= 1

        for i in range(1,102):
            point_map[i] += point_map[i-1]

            if point_map[i] != 0:
                points += 1
        
        return points
