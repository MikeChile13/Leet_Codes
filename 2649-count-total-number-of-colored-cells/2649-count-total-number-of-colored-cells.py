class Solution:
    def coloredCells(self, n: int) -> int:

    # def findN(N):
        if not n:
            return 1
        return self.coloredCells(n-1) + 4*(n-1)
        # print(findN(n))
    
        # S_0 = 1
        # S = 0
        # for N in range(1,n+1):
        #     S = S_0 + 4*(N - 1)
        #     S_0 = S
        # return S
