class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:

        # Returns the first largest valid sequence
        def backtrack(index, used, res):
            if index == len(res):
                # Valid sequence found
                return res

            if res[index]:
                # Value already exist at current index
                # Move to next index
                return backtrack(index + 1, used, res)
            
            for i in range(n, 1, -1):
                if not used[i] and index + i < len(res) and res[index + i] == 0:
                    used[i] = 1
                    res[index] = i
                    res[index + i] = i
                    if backtrack(index + 1, used, res):
                        return res
                    res[index + i] = 0
                    res[index] = 0
                    used[i] = 0

            if not used[1]:
                used[1] = 1
                res[index] = 1
        
                if backtrack(index + 1, used, res):
                    return res
                used[1] = 0
                res[index] = 0

 
        res = [0 for _ in range(2*n)]
        used = [0]*(n + 1)
        
        backtrack(1, used, res)
        return res[1:]