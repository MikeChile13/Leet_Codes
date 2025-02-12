class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums[0] > 0:
            return [num**2 for num in nums]
        if nums[-1] < 0:
            return [num**2 for num in nums][::-1]
        n = len(nums)
        pivot = 0
        for i in range(n):
            if nums[i] >= 0:
                pivot = i
                break
        A = [abs(val) for val in nums[:pivot]][::-1]
        B = nums[pivot:]
        a,b = 0,0
        res = []
        while a < len(A) and b < len(B):
            if A[a] > B[b]:
                res.append(B[b])
                b+=1
            else:
                res.append(A[a])
                a+=1
        # print(res,A,B)
        if a < len(A):
            res.extend(A[a:])
        if b < len(B):
            res.extend(B[b:])
        # print(res)
        return [val**2 for val in res]
