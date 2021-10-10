class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        def search_submatrix(left, up, right, down):
            if left > right or up > down:
                return False
            elif matrix[up][left] > target or matrix[down][right] < target:
                return False
            mid = left + (right - left) // 2
            row = up
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1
                
            return search_submatrix(left, row, mid - 1, down) or search_submatrix(mid + 1, up, right, row - 1)
        
        return search_submatrix(0, 0, len(matrix[0]) - 1, len(matrix) - 1)