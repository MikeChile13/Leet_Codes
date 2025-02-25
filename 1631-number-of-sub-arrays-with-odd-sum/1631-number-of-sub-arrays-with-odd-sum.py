class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        even_count,odd_count = 1,0

        running_sum = 0
        res = 0
        for num in arr:
            running_sum += num
            if running_sum & 1:
                res += even_count
                odd_count +=1
            else:
                res += odd_count
                even_count +=1
        return res%MOD