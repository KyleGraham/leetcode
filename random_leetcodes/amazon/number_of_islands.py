# Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.

# An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. 
# You may assume water is surrounding the grid (i.e., all the edges are water).

# Example 1:
# Input: grid = [
#     ["0","1","1","1","0"],
#     ["0","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"]
#   ]
# Output: 1

# Example 2:
# Input: grid = [
#     ["1","1","0","0","1"],
#     ["1","1","0","0","1"],
#     ["0","0","1","0","0"],
#     ["0","0","0","1","1"]
#   ]
# Output: 4

#solution using bfs
# time complexity: O(m * n) where m is number of rows and n is number of cols
# space complexity: O(m * n)

#if asked to do this with dfs instead, just swap q.popleft() to q.pop() and it will be a dfs iteratively

#essentially we're visiting every item in the grid
#we check if its a 1 and it hasn't been visited yet
# if so, we call the bfs function
#and we increment islands

#first check if the grid is empty
#return 0 if so

#initialize the rows and cols of the grid
#initialize the visit set
#initialize the islands variable to 0

#loop through the rows and cols of the grid
#check if the item is a 1 and not in the visit set
#call the bfs function with the row and col
#increment the islands variable
#return the islands variable

#the bfs function (takes in r, c)
#initialize the queue using deque since python. Remember to use popleft() here

#add the row and col to the visit set
#append the row and col to the queue
#loop through the queue
#pop the left item from the queue to get row and col
#initialize a direction list of lists to [[1, 0], [-1, 0], [0, 1], [0, -1]]
#this will increment the row and col to get the right, left, top, and bottom value
#loop through the directions list
#initialize new row and col variables taking the row/col from the queue and adding the directions row/col
#check all the conditions here
#check if the new row and col are in range of the grid
#check if the item at the new row and col is a 1
#check if the new row and col is not in the visit set

#if so
#append the item to the queue and add the item to the set

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = deque()
            visit.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1

        return islands