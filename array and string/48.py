class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def transpose(matrix):
            N = len(matrix)
            for i in range(N):
                for j in range(i, N):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                    
        def reflect(matrix):
            N = len(matrix)
            for i in range(N):
                for j in range(N // 2):
                    matrix[i][j] , matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]
                    
        transpose(matrix)
        reflect(matrix)