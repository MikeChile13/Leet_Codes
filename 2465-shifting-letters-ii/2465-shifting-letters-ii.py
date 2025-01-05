class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix = [0] * n
        for start, end, direction in shifts:
            if direction:
                prefix[start]+=1
                if end < n-1:
                    prefix[end+1]-=1
            else:
                prefix[start]-=1
                if end < n-1:
                    prefix[end+1]+=1
        prefix_sum = 0
        s = list(s)
        for i in range(n):
            prefix_sum = (prefix_sum + prefix[i]) % 26
            if prefix_sum < 0:
                prefix_sum += 26
            total_shifts = ((ord(s[i]) - 97) + prefix_sum ) % 26
            s[i] = chr(total_shifts + 97)
        return ''.join(s)
