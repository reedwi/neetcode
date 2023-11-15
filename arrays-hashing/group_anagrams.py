from typing import List
from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen_map = defaultdict(list)
        for str in strs:
            sorted_str = tuple(sorted(str))
            seen_map[sorted_str].append(str)
        return list(seen_map.values())

s = Solution()
s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
