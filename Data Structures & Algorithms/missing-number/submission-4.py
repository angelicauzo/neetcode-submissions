class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        n = len(nums)
        # sum from 0 to n whole number divs
        actual_sum = (n *(n + 1)) // 2
        return actual_sum - nums_sum


            
        