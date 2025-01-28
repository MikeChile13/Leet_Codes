class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n,m = len(grid[0]),len(grid)
        max_sum = 0
        def dfs(i,j):
            if i < 0 or i == m or j < 0 or j == n or grid[i][j] == 0:
                return 0
            val = grid[i][j]
            grid[i][j] = 0
            return val + dfs(i+1,j) + dfs(i-1,j) + dfs(i,j+1) + dfs(i,j-1)
        for i in range(m):
            for j in range(n):
                max_sum = max(max_sum,dfs(i,j))
        return max_sum

            