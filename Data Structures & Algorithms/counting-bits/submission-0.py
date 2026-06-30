class Solution:
    def countBits(self, n: int) -> List[int]:
        nums = list(range(n + 1))

        for i in range(n + 1):
            nums[i] = sum(1 for c in bin(i) if c == '1')

        return nums

        
        