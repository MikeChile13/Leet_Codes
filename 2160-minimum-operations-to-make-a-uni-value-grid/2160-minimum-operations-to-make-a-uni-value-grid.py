class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        vals = []
        for row in grid:
            for val in row:
                if abs(val - grid[0][0]) % x != 0:
                    return -1
                vals.append(val)
        vals.sort()
        count = 0
        median = vals[len(vals)//2]
        for val in vals:
            count += abs(median - val)//x
        return count
