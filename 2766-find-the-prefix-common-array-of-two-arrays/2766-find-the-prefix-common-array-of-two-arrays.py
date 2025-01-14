class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        Aset = set()
        Bset = set()
        res = []
        for i in range(len(A)):
            Aset.add(A[i])
            Bset.add(B[i])
            count = 0
            for num in Bset:
                if num in Aset:
                    count+=1
            res.append(count)
        return res
