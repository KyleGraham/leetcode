# using binary search
# time complexity: O(log(m * n)
# space complexity: O(1)

# 3d binary search
# find which array contains the value, find middle point of top and bottom, check if target is less than the first value of the middle array
# if so, move the bottom pointer to the middle - 1
# if not, check if the last value of the middle array is less than the target
# if so, move the top pointer to the middle + 1
# if not, array may contain value, set h (height) to the middle
# then do a regular binary search on the array

#this returns if the value exists, not the indexes, so make sure to check for equality in the else of the regular binary search

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #find which array value contains, like 3d binary search
        t = 0
        b = len(matrix) - 1
        h = -1
        while t <= b:
            m = (t + b) // 2
            if matrix[m][0] > target:
                b = m - 1
            elif matrix[m][len(matrix[m]) -1] < target:
                t = m + 1
            else:
                h = m
                break
        l = 0
        r = len(matrix[h]) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[h][m] > target:
                r = m - 1
            elif matrix[h][m] < target:
                l = m + 1
            else:
                return matrix[h][m] == target
        return False