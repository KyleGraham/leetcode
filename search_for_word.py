# Given a 2-D grid of characters board and a string word, return true if the word is present in the grid, otherwise return false.

# For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. 
# The same cell may not be used more than once in a word.

# Example 1:
# Input: 
# board = [
#   ["A","B","C","D"],
#   ["S","A","A","T"],
#   ["A","C","A","E"]
# ],
# word = "CAT"
# Output: true

# Example 2:
# Input: 
# board = [
#   ["A","B","C","D"],
#   ["S","A","A","T"],
#   ["A","C","A","E"]
# ],
# word = "BAT"
# Output: false



#solution using backtracking
#time complexity: O(n * 4^n)
#space complexity: O(n)

#initialize some constants, ROWS and COLS for the length of the board and length of the board[0]
#initialize a path set, this holds the coordinates of the board that we've visited

#initialize the dfs function with r, c, and i for the row index, col index, and index of the char of the word we're looking for
#check if the index is equal to the length of the word
#return true if it is, we've found the word

#check if the row or col is out of bounds, 
# if the character at the row and col is not the character we're looking for, 
# or if the row and col is in the path set
# return false

#if we get to this point, we know we've found a character in the word
#add the row and col to the path set
#recursively call the function with the left and right of row, and left and right of col. We don't worry about diagnols thankfully
#keep these recursive calls in a variable res with the or condition, so only one needs to return True
#remove the row and col from the path set since we're done with it
#return res

#loop through the rows and cols of the board
#call the dfs function with the row and col and index at 0
#if the dfs function returns True, we've found the word
#return True
#return False if we don't find the word


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            #check out of bounds on row/col
            #check the character we're looking for is not at the r/c location
            #and check if the r/c is in the path set
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path):
                return False

            path.add((r, c))
            res = (dfs(r + 1, c, i +1) or
                    dfs(r - 1, c, i +1) or
                    dfs(r, c + 1, i +1) or
                    dfs(r, c - 1, i +1))
            path.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False

            