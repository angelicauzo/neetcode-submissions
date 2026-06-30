class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        max_height = 0
        max_amount = 0

        while left < right:
            water_height = min(heights[left], heights[right])
            water_amount = water_height * (right - left)

            if water_amount > max_amount:
                max_amount = max(water_amount, max_amount)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return max_amount
