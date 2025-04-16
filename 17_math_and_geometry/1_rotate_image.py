
# Given a square n x n matrix of integers matrix, rotate it by 90 degrees clockwise.

# You must rotate the matrix in-place. Do not allocate another 2D matrix and do the rotation.

# Example 1:
# Input: matrix = [
#   [1,2],
#   [3,4]
# ]
# Output: [
#   [3,1],
#   [4,2]
# ]

# Example 2:
# Input: matrix = [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ]

# Output: [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]

#solution using rotate by four cells
#time complexity: O(n^2) where n is the length of the matrix
#space complexity: O(1)

#essentially, we take the corner cells and rotate them
#then move inward
#then we repeat the process until we reach the center of the matrix

##initialize left and right as 0 and len(matrix) - 1
##while left is less than right
##loop through the range of right - left
#initialize top and bottom as l and r cuz its a square
#save the top left value
#move counterclockwize rotating the values clockwize
#remember to add the i value so that we are moving through the matrix
#matrix[top][l + i]
#matrix[bottom - i][l]
#matrix[bottom][r - i]
#matrix[top + i][r]
#move bottom left into top left
#move bottom right into bottom left
#move top right into bottom right
#move top left into top right
#then decrement right and increment left



class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                # save the topleft
                topLeft = matrix[top][l + i]

                # move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top left into top right
                matrix[top + i][r] = topLeft
            r -= 1
            l += 1