class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)[2:] # skip 0 and 1 as it is 0b which is produced from bin(n)
        n = n.zfill(32) # pad to 32 bits with leading 0s
        n = n[::-1] # reverse the binary string
        return int(n, 2) # num and the base you are converting from
