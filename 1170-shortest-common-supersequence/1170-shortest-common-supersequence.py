from typing import List

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        rows, columns = len(str1), len(str2)

        # Step 1: Compute LCS DP Table
        dp = [[0] * (columns + 1) for _ in range(rows + 1)]
        
        for i in range(1, rows + 1):
            for j in range(1, columns + 1):
                if str1[i - 1] == str2[j - 1]:  # Matching characters
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # Take max of top or left
        
        # Step 2: Backtrack to find LCS
        i, j = rows, columns
        lcs = []
        
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:  # Match found in LCS
                lcs.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:  # Move up
                i -= 1
            else:  # Move left
                j -= 1
        
        lcs.reverse()

        # Step 3: Build the Shortest Common Supersequence
        res = []
        i, j = 0, 0

        for ch in lcs:
            while i < rows and str1[i] != ch:
                res.append(str1[i])
                i += 1
            while j < columns and str2[j] != ch:
                res.append(str2[j])
                j += 1
            res.append(ch)
            i += 1
            j += 1

        # Append remaining characters
        res.extend(str1[i:])
        res.extend(str2[j:])

        return ''.join(res)
