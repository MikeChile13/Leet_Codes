class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        res = [i for i in range(1,n+2)]
        for i in range(n):
            j = i
            while j >= 0 :
                if pattern[j] == 'I' and res[j+1] < res[j]:
                    res[j+1],res[j] = res[j],res[j+1]
                    j-=1
                elif pattern[j] == 'D' and res[j+1] > res[j]:
                    res[j+1],res[j] = res[j],res[j+1]
                    j-=1
                else:
                    break
        return ''.join([str(num) for num in res])