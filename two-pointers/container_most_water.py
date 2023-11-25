class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            max_height = min(height[left], height[right])
            area = max_height * (right - left)
            max_area = max(abs(area), max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area