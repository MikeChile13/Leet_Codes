class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        res = []

        m = len(part)

        for char in s:
            res.append(char)

            # Check if the last m characters in res form `part`
            if len(res) >= m and ''.join(res[-m:]) == part:
                for _ in range(m):
                    res.pop()  # Remove last `m` characters

        return ''.join(res)
