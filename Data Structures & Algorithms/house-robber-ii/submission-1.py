class Solution:
    def rob(self, nums: List[int]) -> int:
        # edge case for a single house:
        if len(nums) == 1:
            return nums[0]

        # can only do nums[0] to nums[n-1]
        # or nums[1] to nums[n]
        prev1_l1 = 0
        prev2_l1 = 0
        for i in range(len(nums) - 1):
            cur_l1 = max(prev1_l1, prev2_l1 + nums[i])
            prev2_l1 = prev1_l1
            prev1_l1 = cur_l1

        prev1_l2 = 0
        prev2_l2 = 0
        for i in range(1, len(nums)):
            cur_l2 = max(prev1_l2, prev2_l2 + nums[i])
            prev2_l2 = prev1_l2
            prev1_l2 = cur_l2
        
        return max(prev1_l1, prev1_l2)
        

        