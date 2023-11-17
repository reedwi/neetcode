from typing import List
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if board[row][col] == '.':
                    continue

                if num in rows[row]:
                    return False
                else:
                    rows[row].add(num)

                if num in cols[col]:
                    return False
                else:
                    cols[col].add(num)

                square_section = (row // 3, col // 3)
                if num in squares[square_section]:
                    return False
                else:
                    squares[square_section].add(num)
        return True
            

board = [
    [".",".","4",".",".",".","6","3","."],
    [".",".",".",".",".",".",".",".","."],
    ["5",".",".",".",".",".",".","9","."],
    [".",".",".","5","6",".",".",".","."],
    ["4",".","3",".",".",".",".",".","1"],
    [".",".",".","7",".",".",".",".","."],
    [".",".",".","5",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."]
]

s = Solution()
val = s.isValidSudoku(board=board)
print(val)