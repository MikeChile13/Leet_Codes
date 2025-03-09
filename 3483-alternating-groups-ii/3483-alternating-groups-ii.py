class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        res = 0
        first = colors[0]

        i = 0

        while i < n:
            j = i + 1
            while j < n and colors[j] != colors[j - 1]:
                j += 1

            count = j - i
            
            if j == n and colors[-1] != first:
                if i == 0:
                    return n
                    
                if colors[0] >= k:
                    res -= colors[0] - k + 1
                count += colors[0]
            
            if count >= k:
                res += count - k + 1

            colors[i] = count
            i = j
   
        return res