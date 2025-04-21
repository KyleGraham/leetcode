# Assume the following rules are for the tic-tac-toe game on an n x n board between two players:

# A move is guaranteed to be valid and is placed on an empty block.
# Once a winning condition is reached, no more moves are allowed.
# A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
# Implement the TicTacToe class:

# TicTacToe(int n) Initializes the object the size of the board n.
# int move(int row, int col, int player) Indicates that the player with id player plays at the cell (row, col) of the board. 
# The move is guaranteed to be a valid move, and the two players alternate in making moves. Return
# 0 if there is no winner after the move,
# 1 if player 1 is the winner after the move, or
# 2 if player 2 is the winner after the move.


#time complexity: O(1)
#space complexity: O(n)

#this leverages the fact that the board is a square
#and keeps track of the total values of rows and cols instead of each individual cell

#rows is just an array of [0] * n
#cols is just an array of [0] * n
#diagonal is a single value
#anti_diagonal is a single value
#the values are incremented by 1 or decremented by -1 depending on the player. 
# that way if one player of each player plays in a row or col, the val will never equal n

#initialize self.n as n, self.rows as [0] * n, self.cols as [0] * n, self.diagonal as 0 and self.anti_diagonal as 0

#move
#set p to 1 if player == 1, else -1
#so player 1 = 1, player 2 = -1
#increment the row and col by p, self.rows[row] += p and self.cols[col] += p
#if the row and col are equal, increment the diagonal by p
#if the row + col == n - 1, increment the anti diagonal by p
#check if the absolute value of the row or col or diagonal or anti diagonal is equal to n
# if so, return the player
# else return 0



class TicTacToe:
  
    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        p = 1 if player == 1 else -1
        self.rows[row] += p
        self.cols[col] += p
        #goes from 0,0, 1,1, 2,2
        if row == col:
            self.diagonal += p
        #goes from 0,2, 1,1, 2,0, so they always = n, which would be 2 here
        if row + col == self.n - 1:
            self.anti_diagonal += p
        
        if (abs(self.rows[row]) == self.n or
            abs(self.cols[col]) == self.n or
            abs(self.diagonal) == self.n or
            abs(self.anti_diagonal) == self.n):
                return player
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)