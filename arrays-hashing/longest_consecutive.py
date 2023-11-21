class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        if nums:
            longest = 1
        else:
            longest = 0
        current_count = 1
        end = False

        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i+1]:
                current_count += 1
            else:
                end = True

            if current_count > longest:
                longest = current_count
            
            if end:
                current_count = 1
                end = False
        return longest
