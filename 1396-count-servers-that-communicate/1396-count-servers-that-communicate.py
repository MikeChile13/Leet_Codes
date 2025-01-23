class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        i = 0
        res = 0
        seenRows = set()
        for row in grid:
            ones = sum(row)
            if ones > 1:
                res+=ones
                seenRows.add(i)
            i+=1
        for column in range(n):
            actual_ones = 0
            total_ones = 0
            for row in range(m):
                total_ones += grid[row][column]
                if row not in seenRows:
                    actual_ones+= grid[row][column]
            if total_ones > 1:
                res += actual_ones
        return res
    