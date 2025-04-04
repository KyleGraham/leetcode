# The n-queens puzzle is the problem of placing n queens on an n x n chessboard so that no two queens can attack each other.

# A queen in a chessboard can attack horizontally, vertically, and diagonally.

# Given an integer n, return all distinct solutions to the n-queens puzzle.

# Each solution contains a unique board layout where the queen pieces are placed. 'Q' indicates a queen and '.' indicates an empty space.

# You may return the answer in any order.

# Example 1:
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There are two different solutions to the 4-queens puzzle.

# Example 2:
# Input: n = 1
# Output: [["Q"]]



#maintain set of cols as queen cant be in same col as other
#check queen position on every row, only one per row
#maintain set of positive diagnols r-1 and c-1
# (r-c) so 0,0 would be 0 diagnol, 0, 1 would be -1, 0,2 would be -2
#maintain set of negative diagnols r+1 and c+1
# (r + c) so 0, 3 would be 3, 0, 2 would be 2, 3 + 1 would be 4, ect

#initialize our sets cols, posDiag (r + c), and negDiag (r - c)
#initialize res as []
#initialize the board as a list of lists with n rows and n cols filled with "." for default

#initialize the backtrack function with r as the current row
#check if the row is equal to n, if so, we've found a solution
#append the current board to the result list and return

#loop through the columns of the board
#check if the column is in the cols set or if the positive or negative diagnols are in the set
#continue if so

#add the column to the cols set, posDiag set, and negDiag set
#add the queen to the board at the current row and column
#call the backtrack function with the next row
#reset the column, posDiag, and negDiag sets
#reset the board at the current row and column to "."

#outside the function, call the backtrack function with row 0
#return res
        
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set() #(r + c)
        negDiag = set() #(r - c)

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = [''.join(row) for row in board]
                res.append(copy) 
                return

            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"
                backtrack(r + 1)
                #reset
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res



        
        
        
        