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

#leetcode solution
#time complexity O(m * n)
#space complexity O(m * n)

#the queue we use here is of rotten oranges instead
#and we keep track of the fresh in a counter
#we use a queue for the fruit that are rotting because if we get them to rotted right away, then the next value may rot earlier than expected

#initialize the rows and cols of the grid
#initialize a deque

#fill the rotten fruit deque and the fresh fruit counter
#loop through rows and cols
#if the val is a 2, add to queue
#otherwise, if the val is a 1, increment the fresh counter
#append a round / level ticker to the queue as (-1, -1)
#initialize minutes to -1
#initialize the directions array
#while the queue is not empty
#pop the left item from the queue to get row and col
#check if the row and col are -1, meaning we finished one round of processing
#increment the minutes
#check if the queue is not empty, to avoid the endless loop
#append (-1, -1) to the queue if so

#otherwise, this is a rotten orange
#then it would contaminate its neighbors
#loop through the directions array
#initialize new row and col variables taking the row/col from the queue and adding the directions row/col
#check that the new row and col are in range of the grid and if the item is a 1 meaning fresh fruit
#if so, it's found a rotten fruit near a fresh fruit thats in bounds
#decrement the fresh counter
#set the item in the grid to 2 meaning rotten fruit
#add item to the rotten fruit queue
#return the minutes if no fresh fruit left, else -1


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()

        # Step 1. build the initial set of rotten oranges
        fresh_oranges = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        # Mark the round / level, _i.e_ the ticker of timestamp
        queue.append((-1, -1))

        # Step 2). start the rotting process via BFS
        minutes_elapsed = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue:
            row, col = queue.popleft()
            if row == -1:
                # We finish one round of processing
                minutes_elapsed += 1
                if queue:  # to avoid the endless loop
                    queue.append((-1, -1))
            else:
                # this is a rotten orange
                # then it would contaminate its neighbors
                for d in directions:
                    neighbor_row, neighbor_col = row + d[0], col + d[1]
                    if ROWS > neighbor_row >= 0 and COLS > neighbor_col >= 0:
                        if grid[neighbor_row][neighbor_col] == 1:
                            # this orange would be contaminated
                            grid[neighbor_row][neighbor_col] = 2
                            fresh_oranges -= 1
                            # this orange would then contaminate other oranges
                            queue.append((neighbor_row, neighbor_col))

        # return elapsed minutes if no fresh orange left
        return minutes_elapsed if fresh_oranges == 0 else -1





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
