class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        
        def is_solvable(board, idx):
            if idx == 81:
                return True
            row = idx // 9
            col = idx % 9
            if board[row][col] != '.':
                return is_solvable(board, idx + 1)
            for i in range(9):
                ch = str(i + 1)
                if ok_to_insert(board, row, col, ch):
                    board[row][col] = ch
                    if is_solvable(board, idx + 1):
                        return True
                    board[row][col] = '.'
            return False
        
        def ok_to_insert(board, i, j, to_insert):
            for row in range(9):
                if board[row][j] == to_insert:
                    return False
            for col in range(9):
                if board[i][col] == to_insert:
                    return False
            for row in range(i//3*3, i//3*3+3):
                for col in range(j//3*3, j//3*3+3):
                    if board[row][col] == to_insert:
                        return False
            return True
        
        if board is None or len(board) != 9 or len(board[0]) != 9:
            return
        is_solvable(board, 0)