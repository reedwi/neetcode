from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_map = {}
        for i, num in enumerate(nums):
            num_to_search = target - num
            if num_to_search in seen_map:
                return [i, seen_map[num_to_search]]
            seen_map[num] = i