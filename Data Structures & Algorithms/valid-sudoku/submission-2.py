class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        flag = True

        for i in range(len(board)):
            row_value = []
            column_value = []

            
            for j in range(len(board)):
                if(board[i][j] != "."):
                    row_value.append(board[i][j])

                if(board[j][i] != "."):
                    column_value.append(board[j][i])
            if len(set(row_value)) != len(row_value) or len(set(column_value)) != len(column_value):
                return False


        
        for box_row in range(0,9,3): #increment 3
            for box_col in range(0,9,3): #increment 3
                box = []

                for i in range(box_row, box_row + 3):
                    for j in range(box_col, box_col + 3):
                        if board[i][j] != ".":
                            box.append(board[i][j])
                if len(set(box)) != len(box):
                    return False
                
        return True        




        
            
                
