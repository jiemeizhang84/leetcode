class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
                
        def ok_to_insert(board, row, col):
            for i in range(row):
                for j in range(len(board)):
                    if board[i][j] == '.':
                        continue
                    if j == col:
                        return False
                    if row - col == i - j:
                        return False
                    if row + col == i + j:
                        return False
            return True
                    
        
        def dfs(row, board, result):
            if row == len(board):
                result.append(strformat(board))
                return
            for col in range(len(board)):
                if not ok_to_insert(board, row, col):
                    continue
                board[row][col] = 'Q'
                dfs(row + 1, board, result)
                board[row][col] = '.'
                
        def strformat(board):
            result = []
            for i in range(len(board)):
                result.append(''.join(board[i]))
            return result  
         
        board = [['.' for i in range(n)] for j in range(n)]
        result = []
        dfs(0, board, result)
        return result