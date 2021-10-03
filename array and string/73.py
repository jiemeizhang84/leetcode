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