class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        R = len(matrix)
        if R == 0:
            return False
        C = len(matrix[0])
        left = 0
        right = R * C - 1
        while left <= right:
            mid = left + (right - left) // 2
            idr = mid // C
            idc = mid % C
            if matrix[idr][idc] == target:
                return True
            elif matrix[idr][idc] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False