# 8.12 Eight Queens
# ==============================================================================================
# Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board so that
# none of them share the same row, column or diagonal. In this case, diagonal means all diagonals,
# not just the two that bisect the board.
# ==============================================================================================
def arrange_queens(row, row_to_cols, board):
    if row == len(row_to_cols):
        board.append(row_to_cols[:]) # done, have all our results
    for col in range(len(row_to_cols)):
        if is_valid(row_to_cols, row, col):
            row_to_cols[row] = col
            arrange_queens(row+1, row_to_cols, board)

def is_valid(row_to_cols, row, col):
    for before_row in range(row):
        before_col = row_to_cols[before_row]
        if before_col == col: # queens in the same column
            return False
        col_distance = abs(before_col - col)
        row_distance = row - before_row
        if row_distance == col_distance: # same diagonal
            return False
    return True

row_to_cols = [0] * 8
board = []
arrange_queens(0, row_to_cols, board)
print board