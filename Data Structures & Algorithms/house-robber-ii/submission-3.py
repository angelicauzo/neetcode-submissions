class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        prev1 = 0
        prev2 = 0
        for i in range(1, len(nums)):
            cur = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = cur

        prev1_2 = 0
        prev2_2 = 0
        for i in range(len(nums) - 1):
            cur_2 = max(prev1_2, prev2_2 + nums[i])
            prev2_2 = prev1_2
            prev1_2 = cur_2

        max_amount = max(prev1, prev1_2)

        return max_amount