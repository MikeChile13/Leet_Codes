class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m = len(grid),len(grid[0])
        count = 0
        def inbound(i,j):
            if (0 <= i < n) and (0 <= j < m):
                return True
            return False
        def dfs(i,j):
            if not inbound(i,j) or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    count+=1
                    dfs(i,j)
        return count
