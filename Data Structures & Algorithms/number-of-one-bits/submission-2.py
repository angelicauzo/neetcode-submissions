class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum(1 for c in bin(n) if c == '1')