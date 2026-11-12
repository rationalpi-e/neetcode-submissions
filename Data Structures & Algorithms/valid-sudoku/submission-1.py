class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sudoku = set()

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    if (i, val) in sudoku or (val, j) in sudoku or (i//3, j//3, val) in sudoku:
                        return False
                sudoku.add((i, val))
                sudoku.add((val, j))
                sudoku.add((i//3, j//3, val))

        return  True