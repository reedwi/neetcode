from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        
        left = 0
        char_frequency = defaultdict(int)
        longest_str = 0
        for right in range(len(s)):
            char_frequency[s[right]] += 1
            cell_difference = right - left + 1
            if cell_difference - max(char_frequency.values()) <= k:
                longest_str = max(longest_str, cell_difference)
            else:
                char_frequency[s[left]] -= 1
                left += 1

        return longest_str