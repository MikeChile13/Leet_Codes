class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        n,m = len(grid[0]),len(grid)
        def dfs(i,j):
            if i < 0 or i == m or j < 0 or j == n or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            return
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    island_count +=1
                    dfs(i,j)
        return island_count
