class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        count = 0
        for i in range(n):
            for j in range(1,n):
                for k in range(2,n):
                    if i < j < k:
                        count += (
                            abs(arr[i] - arr[j]) <= a and
                            abs(arr[j] - arr[k]) <= b and
                            abs(arr[i] - arr[k]) <= c
                        )
        return count
