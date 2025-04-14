# You are given a 2-D grid of integers matrix, where each integer is greater than or equal to 0.

# Return the length of the longest strictly increasing path within matrix.

# From each cell within the path, you can move either horizontally or vertically. You may not move diagonally.

# Example 1:
# Input: matrix = [[5,5,3],[2,3,6],[1,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 3, 6] or [1, 2, 3, 5].

# Example 2:
# Input: matrix = [[1,2,3],[2,1,4],[7,6,5]]
# Output: 7
# Explanation: The longest increasing path is [1, 2, 3, 4, 5, 6, 7].


#soluting using dynamic programming top down
#time complexity: O(n * m) where n is len of matrix and m is len of matrix[0]
#space complexity: O(n * m) where n is len of matrix and m is len of matrix[0]


#initialize rows and cols as the length of the matrix
#initialize dp as a hash, this will hold (r, c) as the key and longest path as the value
#initialize a dfs function that takes in the row, column and previous value
#check if the row and column are out of bounds or if the current value is less than or equal to the previous value
# if so, return 0
#check if the key is in the dp hash, if so return the value
#initialize res as 1
#initialize curVal as the current value
#check the four directions (up, down, left, right) and set res to the max of the dfs of the direction + 1 or res
# set the hash value to res
#return res

#loop through the rows and columns of the matrix and call dfs on each cell with -1 as a prev value
#finally, return the max value in the dp hash


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}

        def dfs(r, c, prevVal):
            if (r < 0 or r == ROWS or
                c < 0 or c == COLS or
                matrix[r][c] <= prevVal):
                    return 0
            if (r, c) in dp:
                return dp[(r, c)]
            
            res = 1
            curVal = matrix[r][c]
            res = max(1 + dfs(r + 1, c, curVal), res)
            res = max(1 + dfs(r - 1, c, curVal), res)
            res = max(1 + dfs(r, c + 1, curVal), res)
            res = max(1 + dfs(r, c - 1, curVal), res)   
            dp[(r, c)] = res
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
        return max(dp.values())