class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        seen = defaultdict(int)
        left = 0
        longest = 0
        for right in range(len(fruits)):
            seen[fruits[right]] += 1
            while len(seen) > 2:
                seen[fruits[left]] -= 1
                if seen[fruits[left]] == 0:
                    del seen[fruits[left]]
                left += 1
            longest = max(longest,right - left + 1)
            
            
        return longest

