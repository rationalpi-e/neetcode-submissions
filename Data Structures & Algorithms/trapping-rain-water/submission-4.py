class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        left_max , right_max , water = 0,0,0

        left  = 0
        right = n-1

        while left < right:
            if height[left] < height[right]:
                left_max= max(height[left], left_max)
                if height[left] < left_max:
                    
                    water += left_max - height[left]

                left  += 1
            else:
                right_max = max(height[right], right_max)
                if height[right] < right_max:
                    
                    water += right_max - height[right]

                right -= 1

        return water 
