class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sudo_set = set()

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    if ((val, i)) in sudo_set or ((j, val)) in sudo_set or ((i//3, j//3 , val)) in sudo_set:
                        return False

                sudo_set.add((val , i))
                sudo_set.add((j, val))
                sudo_set.add((i//3, j//3, val))

        return True