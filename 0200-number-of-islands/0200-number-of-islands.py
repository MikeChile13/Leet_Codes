class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])
        visited = [[False for _  in range(n)] for _ in range(m)]

        # print(visited)
        count = 0
        
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        def dfs(i,j):
            if 0 <= i < m and 0 <= j < n:
                if grid[i][j] == '1' and not visited[i][j]:
                    grid[i][j] = '0'
                    visited[i][j] = True
                    for a,b in dirs:
                        na = a + i
                        nb = b + j
                        if 0 <= na < m and 0 <= nb < n:
                            dfs(na,nb)
            return

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    count += 1
                    dfs(i,j)

        return count