class Solution:
    def countCompleteSubarrays(self, nums):
        distinct = len(set(nums))
        window = defaultdict(int)
        left = 0
        count = 0
        n = len(nums)

        if distinct == 1:
            return n * (n + 1) // 2

        for right in range(n):
            window[nums[right]] += 1
            while len(window) == distinct:
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    del window[nums[left]]
                left += 1
            count += left
        return count
