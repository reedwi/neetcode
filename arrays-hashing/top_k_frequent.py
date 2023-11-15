from typing import List
from collections import Counter, OrderedDict, defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        sorted_counter = OrderedDict(counter.most_common(k))
        return list(sorted_counter.keys())

    def topKFrequentForce(self, nums: List[int], k: int) -> List[int]:
        count_map = defaultdict(int)
        for num in nums:
            count_map[num] += 1
        
        sorted_values = sorted(count_map.values(), reverse=True)
        target_counts = sorted_values[0:k]
        return_list = []
        for num, count in count_map.items():
            if count in target_counts:
                return_list.append(num)
                target_counts.remove(count)
                if not target_counts:
                    return return_list

