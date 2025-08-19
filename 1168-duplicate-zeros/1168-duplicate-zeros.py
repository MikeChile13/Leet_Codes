class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        dummy = []
        n = len(arr)
        for num in arr:
            if num:
                dummy.append(num)
            else:
                dummy.append(0)
                dummy.append(0)
            if len(dummy) == n:
                break
        for i in range(n):
            arr[i] = dummy[i]
        dummy.clear()
