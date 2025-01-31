class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        n = len(grid)
        islands = dict()
        representatives = dict()

        def dfs(curr_i,curr_j,start_i,start_j):
            if curr_i < 0 or curr_i == n or curr_j < 0 or curr_j == n or grid[curr_i][curr_j] != 1:
                return 0
            representatives[(curr_i,curr_j)] = (start_i,start_j)
            grid[curr_i][curr_j] = 2
            return ( 1 + dfs(curr_i+1,curr_j,start_i,start_j) +
            dfs(curr_i-1,curr_j,start_i,start_j) +
            dfs(curr_i,curr_j+1,start_i,start_j) +
            dfs(curr_i,curr_j-1,start_i,start_j) )

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    size = dfs(i,j,i,j)
                    islands[(i,j)] = size   
        res = 0
        if len(representatives) == 0:
            return 1
        if len(representatives) == n*n:
            return n*n
            
        for i in range(n):
            for j in range(n):
                if not grid[i][j]:
                    surroundings = set()
                    size = 0
                    moves = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
                    for row,col in moves:
                        rep = representatives.get((row,col),(-1,-1))
                        if rep not in surroundings:
                            size += islands.get(rep,0)
                            surroundings.add(rep)
                    res = max(res, size+1)
     
        return res