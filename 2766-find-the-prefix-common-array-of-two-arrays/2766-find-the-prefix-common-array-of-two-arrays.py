class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        found = set()
        res = []
        prefix = 0
        for i in range(len(A)):
            if A[i] in found:
                prefix +=1
            else:
                found.add(A[i])
            if B[i] in found:
                prefix +=1
            else:
                found.add(B[i])
            res.append(prefix)
        return res