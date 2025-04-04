# You are given a 
# m×n 2D grid initialized with these three possible values:

# -1 - A water cell that can not be traversed.
# 0 - A treasure chest.
# INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
# Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest than the value should remain INF.

# Assume the grid can only be traversed up, down, left, or right.

# Modify the grid in-place.

# Example 1:

# Input: [
#   [2147483647,-1,0,2147483647],
#   [2147483647,2147483647,2147483647,-1],
#   [2147483647,-1,2147483647,-1],
#   [0,-1,2147483647,2147483647]
# ]

# Output: [
#   [3,-1,0,1],
#   [2,2,1,-1],
#   [1,-1,2,-1],
#   [0,-1,3,4]
# ]
# Example 2:

# Input: [
#   [0,-1],
#   [2147483647,2147483647]
# ]

# Output: [
#   [0,-1],
#   [1,2]
# ]

#multi source bfs solution
#start bfs from every treasure and mark the distance to each land
#time complexity (O(m * n)) where m is number of rows and n is number of cols
#space complexity (O(m * n)) where m is number of rows and n is number of cols

#I like initializing the possible values for land, water, and treasure as class variables
#that way they're not just magic numbers
#initialize rows and cols to the len of rows and cols
#initialize the visit set
#initialize the queue using deque since python. Remember to use popleft() here

#loop through the rows and cols of the grid
#check if the item is a treasure
#if so, add to the queue and the visit set

#initialize the distance variable to 0
#while the queue is not empty
#loop through the queue. This gets the full layer of the queue. So initially treasures are added. Then all lands 1 distance from treasures. 
#popleft from the queue
#set the value of grid[r][c] to the distance. Initially distance is 0, so all treasures are set to 0 which they are anyways

#call the addLand function on all 4 directions
#increment the distance variable outside the for loop

#addland function
#will check if the row and col are out of bounds, in the visit queue, or if the item is water
# if so, return
#otherwise, add the row and col to the visit set and append it to the queue



class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        self.land = 2147483647
        self.water = -1
        self.treasure = 0
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        q = deque()

        def addLand(r, c):
            if (r < 0 or r == rows or c < 0 or c == cols or
                 (r, c) in visit or grid[r][c] == self.water):
                 return
            visit.add((r, c))
            q.append((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == self.treasure:
                    q.append((r, c))
                    visit.add((r, c))
        dist = 0
        while q:
            for i in range(len(q)):  #gets the full layer of the q
                r, c = q.popleft()
                grid[r][c] = dist #will be all treasures initially, so just resetting to 0
                
                addLand(r + 1, c)
                addLand(r - 1, c)
                addLand(r, c + 1)
                addLand(r, c - 1)
            dist += 1
        

#bfs solution not optimal
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        self.land = 2147483647
        self.water = -1
        self.treasure = 0
        self.directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            min_dist = float('infinity')
            q = deque()
            q.append((r, c))
            visit = [[False] * cols for _ in range(rows)]
            visit[r][c] = True
            dist = 0
            while q:
                #not sure why this for loop is necessary. Maybe to check all steps before incrementing the distance
                #yeah, checks all the steps added by the directions before moving onto any that were correct from the directions
                for _ in range(len(q)):
                    row, col = q.popleft()
                    if grid[row][col] == self.treasure:
                        return dist
                    for dr, dc in self.directions:
                        r = row + dr
                        c = col + dc
                        if (r in range(rows) and 
                            c in range(cols) and 
                            grid[r][c] != self.water and not
                            visit[r][c]):
                                visit[r][c] = True
                                q.append((r, c))
                dist += 1
            return self.land
                            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == self.land:
                    grid[r][c] = bfs(r, c)