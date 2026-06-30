class Solution:
    def getSum(self, a: int, b: int) -> int:
        # solve using bit manipulation
        mask = 0xFFFFFFFF # hexadecimal which translates to 32 1's in binary

        # XOR - if a is 0 and b is 1 a^b is 1 and if they are both 1 or 0, a^b = 0

        # is a AND b are 1, we know we will have a 1 carry operator
        # need to shift it to the left by 1

        while b & mask:
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        return a if b == 0 else ~(a ^ mask) 
        # ~(a ^ mask) handles negative results — converts back from Python's 
        # representation to the correct signed integer.