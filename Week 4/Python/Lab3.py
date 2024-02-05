# Added since the matrixInPlace was using the output matrix from the rotateMatrix function
import copy


# This function takes a 2D array and rotates it 90 degrees clockwise with a new matrix
def rotateMatrix(matrix):
    num_Row = len(matrix)
    # Show the original matrix
    print("Stage 1: ")
    for row in matrix:
        print(row)
    # Copy the original matrix to a new matrix but with all elements set to 0
    newMatrix = [[0 for i in range(num_Row)] for j in range(num_Row)]
    # Then rotate the new matrix
    for i in range(num_Row):
        for j in range(num_Row):
            # n - 1 - i is the row index in the new matrix
            newMatrix[j][num_Row - 1 - i] = matrix[i][j]
    # Show the new matrix
    print("\nStage 2: ")
    for row in newMatrix:
        print(row)
    # Afater rotating, copy the new matrix back to the original matrix
    for i in range(num_Row):
        for j in range(num_Row):
            matrix[i][j] = newMatrix[i][j]
    # Show the end result
    print("\nStage 3: ")
    for row in matrix:
        print(row)
    return matrix

# This function takes a 2D array and rotates it 90 degrees clockwise in place (without using a new matrix)


def rotateInPlace(matrix):
    num_Row = len(matrix)
    # Show the original matrix
    print("Stage 1: ")
    for row in matrix:
        print(row)
    # Swap the rows and columns
    for i in range(num_Row):
        for j in range(i, num_Row):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Show the new matrix
    print("\nStage 2: ")
    for row in matrix:
        print(row)
    # Reverse each row
    for i in range(num_Row):
        matrix[i] = matrix[i][::-1]
    # Show the end result
    print("\nStage 3: ")
    for row in matrix:
        print(row)
    return matrix


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
matrix_copy = copy.deepcopy(matrix)

print("\nRotated matrix:")
rotatedMatrix = rotateMatrix(matrix)

print("\nRotated matrix in place:")
rotatedMatrixInPlace = rotateInPlace(matrix_copy)

#Time complexity: O(n^2) since we are iterating through the matrix twice
#Space complexity: O(n^2) since we are creating a new matrix with the same size as the original matrix

'''
Simulation:
matrix =[[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

def rotateMatrix(matrix):
num_Row = 3 since the three rows are    [1, 2, 3] 1 row
                                        [4, 5, 6] 2 row
                                        [7, 8, 9] 3 row
newMatrix = [[0, 0, 0]
            [0, 0, 0]
            [0, 0, 0]]
for i in range(3):
    for j in range(3):
        newMatrix[j][3 - 1 - i] = matrix[i][j]
        newMatrix = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
Turning [1,2,3] into    [7,4,1]
        [4,5,6]         [8,5,2]
        [7,8,9]         [9,6,3]
        
def rotateInPlace(matrix):
num_Row = 3 since the three rows are    [1, 2, 3] 1 row
                                        [4, 5, 6] 2 row
                                        [7, 8, 9] 3 row
for i in range(3):
    for j in range(i, 3):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        matrix =    [[1, 4, 7]
                    [2, 5, 8]
                    [3, 6, 9]]
Then for i in range(3): it will reverse each row
    matrix[i] = matrix[i][::-1]
    matrix =    [[7, 4, 1]
                [8, 5, 2]
                [9, 6, 3]]

'''
