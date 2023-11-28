class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pairs = [[pos, _speed] for pos, _speed in zip(position, speed)]
        stack = []

        for pos, s in sorted(pairs)[::-1]:
            stack.append((target - pos) / s)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)