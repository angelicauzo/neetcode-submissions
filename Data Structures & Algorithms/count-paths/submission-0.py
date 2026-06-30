class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # best approach is dynamic programming
        # dp = [1] * n creates a single row of size n
        dp = [[1] * n for _ in range(m)] 
        # creating a solution grid of m * n
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]
        