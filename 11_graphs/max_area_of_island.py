

#solution using bfs
# time complexity: O(m * n) where m is number of rows and n is number of cols
# space complexity: O(m * n)

#really similar to count_number_of_islands.py only we're getting the max area of any island
# #if asked to do this with dfs instead, just swap q.popleft() to q.pop() and it will be a dfs iteratively

#first check if the grid is empty
#return 0 if so

#initialize the rows and cols of the grid
#initialize the visit set
#initialize the maxArea variable to 0. Set it to a class variable so we can access it in the bfs function

#loop through the rows and cols of the grid
#check if the item is a 1 and not in the visit set
#call the bfs function with the row and col, and the area set to 0 since its a fresh island

#return the maxArea variable

#the bfs function (takes in r, c, and area)
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
#increment the function area variable by 1
#then set the maxArea variable to the max of the area and maxArea


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        self.maxArea = 0

        def bfs(r, c, area):
            q = deque()
            visit.add((r, c))
            q.append((r, c))
            area += 1
            self.maxArea = max(area, self.maxArea)
            
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if (r in range(rows) and 
                        c in range(cols) and
                        (r, c) not in visit and
                        grid[r][c] == 1):
                        q.append((r, c))
                        visit.add((r, c))
                        area += 1
                        self.maxArea = max(area, self.maxArea)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    bfs(r, c, 0)
        
        return self.maxArea 