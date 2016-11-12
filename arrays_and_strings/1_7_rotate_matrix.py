# 1.7 Rotate Matrix
# ==============================================================================================
# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a
# method to rotate the image by 90 degrees. Can you do this in place?
# ==============================================================================================
def rotate_matrix(matrix):
    l = len(matrix) - 1
    for layer in range(len(matrix)/2):
        for offset in range(layer,len(matrix)-layer-1):
            temp = matrix[layer][offset]
            matrix[layer][offset] = matrix[offset][l-layer]
            matrix[offset][l-layer] = matrix[l-layer][l-offset]
            matrix[l-layer][l-offset] = matrix[l-offset][layer]
            matrix[l-offset][layer] = temp
    return matrix

matrix = [[1,1,1,1],
          [2,2,2,2],
          [3,3,3,3],
          [4,4,4,4]]

result = rotate_matrix(matrix)
for i in result:
    print i