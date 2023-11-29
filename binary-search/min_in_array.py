class Solution:
    def findMin(self, nums: list[int]) -> int:
        for i, val in enumerate(nums):
            if i > 0 and val < nums[i-1]:
                return val
        return nums[0]
    
class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        min_val = nums[0]
        while left <= right:
            if nums[left] < nums[right]:
                min_val = min(min_val, nums[left])
            mid = (left + right) // 2
            min_val = min(min_val, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        return min_val