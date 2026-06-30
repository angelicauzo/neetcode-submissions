class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # backtracking and ...
        result = []

        def backtrack(i, current, total):
            if total == target:
                result.append(current[:]) # this will add a copy
                return
            
            if total > target or i > len(nums) - 1:
                return

            # include nums[i] , stay at i and allow reuse
            current.append(nums[i])
            backtrack(i, current, total + nums[i])
            current.pop() # cleanup after backtrack

            # skip nums[i] and move to i+1
            backtrack(i + 1, current, total)

        backtrack(0, [], 0)
        return result