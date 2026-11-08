class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n-1
        max_water = 0

        while left < right:
            cur_water = min(heights[left], heights[right]) * abs(left-right)
            max_water = max(cur_water, max_water)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_water