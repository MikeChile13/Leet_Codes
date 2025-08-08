# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:

#         dp = [[float('inf')] * (len(word2) + 1) for _ in range(len(word1) + 1)]
#         #base case of 2D array
#         for j in range(len(word2) + 1):
#             dp[len(word1)][j] = len(word2) - j

#         for i in range(len(word1) + 1):
#             dp[i][len(word2)] = len(word1) - i

#         #bottom up
#         for i in range(len(word1) - 1, - 1, -1):
#             for j in range(len(word2) - 1, - 1, -1):
#                 if word1[i] == word2[j]:
#                     dp[i][j] = dp[i+1][j+1]
#                 else:
#                     dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j+1], dp[i+1][j+1])
        
#         return dp[0][0]

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        row, col = len(word1), len(word2)
        # dp[i][j] = edit distance between first i chars of word1 and first j chars of word2
        dp = [[0] * (col + 1) for _ in range(row + 1)]

        # case 1: what if word one was empty?
        # -> insert every character in word2 
        # the following just represents that case 
        for j in range(col + 1):
            dp[0][j] = j  # j insertions needed


        # Fill the DP table
        for i in range(1, row + 1):
            dp[i][0] = i    # i deleations needed
            for j in range(1, col + 1):
                if word1[i - 1] == word2[j - 1]:
                    # Characters match, no operation needed
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],     # dp[i-1][j]   -> delete from word1
                        dp[i][j - 1],     # dp[i][j-1]   -> insert into word1
                        dp[i - 1][j - 1]  # dp[i-1][j-1] -> replace in word1
                    )

        return dp[row][col]
