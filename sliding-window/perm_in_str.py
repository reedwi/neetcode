class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        str_len = len(s2)
        
        for i in range(str_len - window + 1):
            perm = True
            str_window = s2[i:i+window]
            for letter in s1:
                if letter in str_window:
                    str_window = str_window.replace(letter, '', 1)
                    continue
                else:
                    perm = False

            if perm:
                return True
        return False
