class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        point_map = defaultdict(int)
        points = 0
        bottom,top = float('inf'),float('-inf')
        for start, end in nums:
            point_map[start] += 1
            point_map[end + 1] -= 1
            bottom = min(start,bottom)
            top = max(end,top)

        coverage = 0
        for i in range(bottom, top+1):
            coverage += point_map[i]
            if coverage > 0:
                points += 1

        return points
