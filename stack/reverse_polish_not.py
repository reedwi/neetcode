class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            match token:
                case '+':
                    val = stack.pop() + stack.pop()
                    stack.append(val)
                case '-':
                    a, b = stack.pop(), stack.pop()
                    val = b - a
                    stack.append(val)
                case '*':
                    val = stack.pop() * stack.pop()
                    stack.append(val)
                case '/':
                    a, b = stack.pop(), stack.pop()
                    val = b / a
                    stack.append(int(val))
                case _:
                    stack.append(int(token))
        return stack[0]