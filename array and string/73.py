class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C = len(matrix[0])
        
        col_flag = False
        
        for i in range(R):
            if matrix[i][0] == 0:
                col_flag = True
            for j in range(1, C):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        for i in range(1, R):
            for j in range(1, C):                
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0
                    
        if col_flag == True:
            for i in range(R):
                matrix[i][0] = 0

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])
        row_zero = False        
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        row_zero = True                        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0 :
                    matrix[r][c] = 0                    
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        if row_zero:
            for c in range(COLS):
                matrix[0][c] = 0