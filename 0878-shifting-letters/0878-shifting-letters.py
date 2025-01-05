class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        s = list(s)
        shift = 0
        for i in range(len(shifts)-1,-1,-1):
            shift+=shifts[i]
            s[i] = chr((ord(s[i]) - 97 + shift) % 26 + 97 )
        return ''.join(s)