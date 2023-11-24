class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([letter for letter in s if letter.isalnum()]).lower()
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True
            
        