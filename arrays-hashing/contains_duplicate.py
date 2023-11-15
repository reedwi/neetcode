from typing import List
class Solution:
    def contains_duplicate_set(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        if len(set_nums) < len(nums):
            return True
        else:
            return False
    
    def contains_duplicate_hash_set(self, nums: List[int]) -> bool:
        seen_nums = set()
        for num in nums:
            if num in seen_nums:
                return True
            else:
                seen_nums.add(num)