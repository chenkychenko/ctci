# 1.8 Zero Matrix
# ==============================================================================================
# Write an algorithm wuch that if an element in an MxN matrix is 0, its entire row and column
# are set to 0.
# ==============================================================================================
def zero_matrix(matrix):
    zero_columns = set()
    zero_rows = set()
    for m in range(len(matrix)):
        for n in range(len(matrix[m])):
            if matrix[m][n] == 0:
                zero_rows.add(m)
                zero_columns.add(n)
    for col in zero_columns:
        make_col_zero(matrix, col)
    for row in zero_rows:
        make_row_zero(matrix, row)
    return matrix
        
def make_col_zero(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0

def make_row_zero(matrix, row):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0

matrix = [[1,2,3,6],
          [4,0,6,0],
          [7,8,9,3]]

for i in zero_matrix(matrix):
    print i