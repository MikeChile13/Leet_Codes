class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        #similar to approach 2 of the editorial, but with different positions map.
        rows,cols = len(mat),len(mat[0])

        cols_count = [rows]*cols
        rows_count = [cols]*rows
        positions = {}

        for r in range(rows):
            for c in range(cols):
                positions[mat[r][c]] = (r,c)

        for i,val in enumerate(arr):
            r,c = positions[val]
            rows_count[r] -= 1
            cols_count[c] -= 1

            if rows_count[r] == 0 or cols_count[c] == 0:
                return i

        return -1