class Solution:
    def hammingWeight(self, n: int) -> int:
        # take the sum of all the digits
        
        return sum(1 for c in bin(n) if c == '1')