class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_area = 0
        stack = []
        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                idx, h = stack.pop()
                max_area = max(max_area, h * (i - idx))
                start = idx
            stack.append((start, height))
        
        for i, height in stack:
            max_area = max(max_area, height * (len(heights) - i))
        
        return max_area