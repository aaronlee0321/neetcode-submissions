from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #test in 9 box
        boxes_idx = [[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
        for row,col in boxes_idx:
            entries = []
            entries.append(board[row][col])
            
            entries.append(board[row][col + 1])
            entries.append(board[row][col + 2])

            entries.append(board[row + 1][col])
            entries.append(board[row + 2][col])

            entries.append(board[row + 1][col + 1])
            entries.append(board[row + 2][col + 2])

            entries.append(board[row + 1][col + 2])
            entries.append(board[row + 2][col + 1])

            filtered_entries = []
            for entry in entries:
                if entry != '.':
                    filtered_entries.append(entry)
            
            if len(filtered_entries) != len(set(filtered_entries)):
                print(row,col,filtered_entries)
                return False

        
        for idx in range(9):
            rows = []
            cols = []

            for cell in range(9):
                curr_row = board[idx][cell]
                if curr_row != '.':
                    rows.append(curr_row)

                col_row = board[cell][idx]
                if col_row != '.':
                    cols.append(col_row)
                
            if len(rows) != len(set(rows)):
                return False
            if len(cols) != len(set(cols)):
                return False

        return True            

            
