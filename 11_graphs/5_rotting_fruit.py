# You are given a 2-D matrix grid. Each cell can have one of three possible values:

# 0 representing an empty cell
# 1 representing a fresh fruit
# 2 representing a rotten fruit
# Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit also becomes rotten.

# Return the minimum number of minutes that must elapse until there are zero fresh fruits remaining. If this state is impossible within the grid, return -1.

# Example 1:
# Input: grid = [[1,1,0],[0,1,1],[0,1,2]]
# Output: 4

# Example 2:
# Input: grid = [[1,0,1],[0,2,0],[1,0,1]]
# Output: -1

#bfs solution using 2 deques
#time complexity O(m * n)
#space complexity O(m * n)

#initialize the rows and cols of the grid
#initialize the directions array
#initialize the queue using deque since python. Remember to use popleft() here

#loop through eveyr row and col
#check if the item is a 1 meaning fresh fruit
#if so, add it to the queue

#initialize minutes to 0
#while q:
#initialize a rottenQ using deque, this will be the amount of fruit that rotted this minute/round
#for loop on the length of the queue, this will get all the fresh fruit for the round
#pop the left item from the queue to get row and col
#initialize fresh variable to True
#loop through the directions list
#initialize new row and col variables taking the row/col from the queue and adding the directions row/col
#check that the new row and col are in range of the grid and if the item is a 2 meaning rotten fruit
#if so, it's found a rotten fruit near a fresh fruit thats in bounds
#set fresh to False

#outside the directions loop, 
#check if fresh is still True
# if so, append the row and col to the queue
#otherwise, append the row and col to the rottenQ

#outside of the for loop/round
#increment minutes
#check if the len of rottenQ is empty. No fruit rotted if so, return -1 edge case 

#while rottedQ
#pop the left item from the queue to get row and col
# set the item in the grid to 2 meaning rotten fruit
#return minutes

#we use a queue for the fruit that are rotting because if we get them to rotted right away, then the next value may rot earlier than expected 

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #another multi source bfs solution
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    q.append((r, c))
        minutes = 0
        while q:
            rottenQ = deque()
            for i in range(len(q)):
                row, col = q.popleft()
                fresh = True
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == 2):
                            fresh = False
                if fresh:
                    q.append((row, col))
                else:
                    rottenQ.append((row, col))
            minutes += 1
            if len(rottenQ) == 0:
                return -1
            while rottenQ:
                r, c = rottenQ.popleft()
                grid[r][c] = 2
        return minutes
