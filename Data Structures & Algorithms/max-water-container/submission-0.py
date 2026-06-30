class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_water = 0

        while left < right:
            water_height = min(heights[left], heights[right])
            water_stored = water_height * (right - left)
            if water_stored > max_water:
                max_water = max(max_water, water_stored)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            

        return max_water


        