# Given an m x n matrix of integers matrix, if an element is 0, set its entire row and column to 0's.

# You must update the matrix in-place.

# Follow up: Could you solve it using O(1) space?

# Example 1:
# Input: matrix = [
#   [0,1],
#   [1,0]
# ]
# Output: [
#   [0,0],
#   [0,0]
# ]

# Example 2:
# Input: matrix = [
#   [1,2,3],
#   [4,0,5],
#   [6,7,8]
# ]
# Output: [
#   [1,0,3],
#   [0,0,0],
#   [6,0,8]
# ]

#0(1) space solution
#time complexity: O(m * n) where m is len of matrix and n is len of matrix[0]
#space complexity: O(1)

#only need extra space for the first row and first column, we use a bool
#otherwise we set the first value of the row/col that needs to be zeroed to zero
#this is because we've already gone over those values

#initialize rowZero as False
#initialize ROWS as len(matrix) and COLS as len(matrix[0])

#loop through r in range(ROWS)
#loop through c in range(COLS)
#check if matrix[r][c] == 0
# if so, set matrix[0][c] = 0
# if r > 0, set matrix[r][0] = 0
# else set rowZero = True
#loop through r in range(1, ROWS)
#loop through c in range(1, COLS)
#check if matrix[0][c] == 0 or matrix[r][0] == 0
# if so, set matrix[r][c] = 0
#check if matrix[0][0] == 0
# if so, loop through r in range(ROWS) and set matrix[r][0] = 0
#check if rowZero is True
# if so, loop through c in range(COLS) and set matrix[0][c] = 0



class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        rowZero = False
        #determine which rows and cols need to be zero
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0
                


        




# My brute force solution. takes O(n) memory where n is the number of zeroes

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroHash = {}

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroHash[(i, j)] = 0
        for r, c in zeroHash.keys():
            for j in range(len(matrix[0])):
                matrix[r][j] = 0
            for i in range(len(matrix)):
                matrix[i][c] = 0