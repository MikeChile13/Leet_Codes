class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if not num:
            return [-1,0,1]
        start = 0
        left = 0 
        right = num
        while left <= right:
            mid = (left + right) // 2
            total = 3 * mid + 3

            if total == num:
                return [mid, mid + 1, mid + 2]
            elif total < num:
                left = mid + 1
            else:
                right = mid - 1
        return []