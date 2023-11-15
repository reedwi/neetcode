from collections import defaultdict, Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        if sorted_t == sorted_s:
            return True
        
    def isAnagramHash(self, s: str, t: str) -> bool:
        char_count = defaultdict(int)

        for char in s:
            char_count[char] += 1

        for char in t:
            char_count[char] -= 1

        for count in char_count.values():
            if count != 0:
                return False
        
        return True
    
    def isAnagramCounter(self, s: str, t: str) -> bool:
        s_counter = Counter(s)
        t_counter = Counter(t)

        if s_counter == t_counter:
            return True