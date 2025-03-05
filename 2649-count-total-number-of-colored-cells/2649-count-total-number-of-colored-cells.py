class Solution:
    def coloredCells(self, n: int) -> int:
    #     if not n:
    #         return 1
    #     return self.coloredCells(n-1) + 4*(n-1)
    #     print(findN(n))

        # S = 1
        # for N in range(2,n+1):
        #     S = S + 4*(N - 1)
        # return S
        return 2 * (n-1) * n + 1

