class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1 
        
        while left <= right:
            
            mid = (right + left ) // 2
            
            if nums[mid] == target:
                return mid 
            # LEFT SORTED PORTION
            elif nums[left]<=nums[mid]:
                if target > nums[mid] or target < nums[left]:
                     left = mid + 1
                else:
                    right = mid -1
            # RIGHT SORTED PORTION
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid -1 
                else:
                     left = mid+1
                    
        
        return -1