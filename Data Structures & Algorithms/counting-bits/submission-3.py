class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)
        for i in range(n + 1):
            output[i] = sum(1 for c in bin(i) if c == '1')

        return output