class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev = -1
        for string in s.split(' '):
            if string.isnumeric():
                val = int(string)
                if val <= prev:
                    return False
                prev = val
        return True