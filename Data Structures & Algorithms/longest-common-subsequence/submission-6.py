class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dynamic programmming
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        # base case dp[0][0] = 0 - empty string

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i-1] == text2[j-1]: # this is refering to character at i
                # recall we added one to the matrix for the empty set
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        return dp[len(text1)][len(text2)]