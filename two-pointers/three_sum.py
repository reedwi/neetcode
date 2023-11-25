class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets = []
        nums.sort()

        nums_len = len(nums) - 1
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            left, right = i + 1, nums_len
            while left < right:
                curr_val = num + nums[left] + nums[right]
                if curr_val < 0:
                    left += 1
                elif curr_val > 0:
                    right -= 1
                else:
                    triplets.append([num, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left +=1
        return triplets