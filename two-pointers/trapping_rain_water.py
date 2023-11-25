class Solution:
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        units = 0

        while left < right:
            if max_left < max_right:
                left += 1
                max_left = max(max_left, height[left])
                units += max_left - height[left]
            else:
                right -= 1
                max_right = max(max_right, height[right])
                units += max_right - height[right]
        return units