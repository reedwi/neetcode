class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        result = []

        def backtrack(open_parens, closed_parens):
            if open_parens == n == closed_parens:
                result.append(''.join(stack))
                return
            
            if open_parens < n:
                stack.append('(')
                backtrack(open_parens + 1, closed_parens)
                stack.pop()
            
            if closed_parens < open_parens:
                stack.append(')')
                backtrack(open_parens, closed_parens + 1)
                stack.pop()
        
        backtrack(0,0)
        return result