
# There is an m x n grid where you are allowed to move either down or to the right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that can be taken 
# from the top-left corner of the grid (grid[0][0]) to the bottom-right corner (grid[m - 1][n - 1]).

# You may assume the output will fit in a 32-bit integer.

# Example 1:



# Input: m = 3, n = 6

# Output: 21
# Example 2:

# Input: m = 3, n = 3

# Output: 6

#Solution using dynamic programming bottom up
#time complexity: O(n * m) where n is len of nums and m is target
#space complexity: O(n)

#this works by calculaing the number of options starting from the finish (n-1, m-1)
#it adds the number of options from the right and down
#the bottom row is always 1 since there is only one way to get to the end, so that is defaulted to 1
# then the next row is calculated
# we only keep track of 2 rows at a time since that's all we need

#at the end, we return the top left cell, which is the number of options to get to the end

#initialzie row as [1]  * n, this is the bottom row
#loop through the rows from the bottom to the top, with - 1 added since the bottom row is already set
#initialize newRow as [1] * n, this is the current row
#loop through the columns from the right to the left
#for each column, set the current cell to the sum of the right and down cells
#at the end of the row, set row to newRow
#return the top left cell, which is the number of options to get to the end


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]
    


#bullshit solution using factorial
# Time complexity: O((M+N)(log(M+N)loglog(M+N)) ^ 2)
# Space complexity: O(1)

from math import factorial


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return factorial(m + n - 2) // factorial(n - 1) // factorial(m - 1)