

#solution using iteration
#time complexity: O(m * n) where m is len of matrix and n is len of matrix[0]
#space complexity: O(1)

#Essentially we want to return the values in the matrix in a spiral order
#so top row is left to right
#then right column top to bottom
#then bottom row right to left
#then left column bottom to top
#when we do one step, we increment/decrement the corresponding row or col that was just used

#so top row left to right, we increment top by 1
#right column top to bottom, we decrement right by 1
#bottom row right to left, we decrement bottom by 1
#left column bottom to top, we increment left by 1

#we want to check out of bounds halfway through for edge cases

##initialize res as an empty array
##initialize left and right as 0 and len(matrix[0])
##initialize top and bottom as 0 and len(matrix)
##while left is less than right and top is less than bottom
##loop through the range of left to right
##append the top row to res, so res.append(matrix[top][i])
##increment top by 1
##loop through the range of top to bottom
##append the right column to res, so res.append(matrix[i][right - 1])
##decrement right by 1
##check halfway through just in case something like only 1 row matrix
##loop through the range of right - 1 to left - 1
##append the bottom row to res, so res.append(matrix[bottom - 1][i])
##decrement bottom by 1
##loop through the first col so  range of bottom - 1 to top - 1
##append the left column to res, so res.append(matrix[i][left])
##increment left by 1

#return res

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            #get every value in the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            #check halfway through just incase something like only 1 row matrix
            if not (left < right and top < bottom):
                break
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res