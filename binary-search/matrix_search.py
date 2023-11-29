class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for num_set in matrix:
            low = 0
            high = len(num_set) - 1

            while low <= high:
                mid = low + (high - low) // 2

                if num_set[mid] == target:
                    return True
                
                elif num_set[mid] < target:
                    low = mid + 1

                else:
                    high = mid - 1
        return False

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        left, right = 0, rows * cols - 1
        while left <= right:
            mid = (left + right) // 2
            
            mid_row, mid_col = divmod(mid, cols)

            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] < target:
                left = mid + 1
            else:
                right = mid -1
        
        return False