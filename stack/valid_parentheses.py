class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {
            '(':')', 
            '{':'}',
            '[':']'
        }
        stack = []

        for char in s:
            if char in char_map:
                stack.append(char)
                continue
            elif len(stack) == 0 or char_map[stack.pop()] != char:
                return False

        return not stack