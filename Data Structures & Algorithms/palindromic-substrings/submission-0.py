class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)

        for left in range(n):
            for right in range(left, n):
                x = s[left: right + 1]
                if x == x[::-1]:
                    count += 1

        return count
        