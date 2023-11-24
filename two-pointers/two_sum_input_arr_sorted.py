class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        seen_values = {}
        for i, num in enumerate(numbers, 1):
            target_val = target - num
            if target_val in seen_values:
                location = seen_values[target_val]
                return [location, i]
            else:
                seen_values[num] = i

        