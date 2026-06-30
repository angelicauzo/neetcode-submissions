class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Solve by dynamic programming
        dp = [False] * (len(s) + 1) 
        # dp[i] means "can the first i characters of s 
        # be segmented using dictionary words?
        dp[0] = True
        for i in range(1, len(s) + 1):
            for word in wordDict:
                if i >= len(word) and dp[i - len(word)]:
                    if s[i-len(word):i] == word:
                        dp[i] = True
        return dp[len(s)]