import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        output = []

        for i in range(len(nums)):
            prefix.append(math.prod(nums[:i]))
            postfix.append(math.prod(nums[i+1:]))
            output.append(prefix[i] * postfix[i])

        return output

