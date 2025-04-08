
# You are given a square 2-D matrix of distinct integers grid where each integer grid[i][j] represents the elevation at position (i, j).

# Rain starts to fall at time = 0, which causes the water level to rise. At time t, the water level across the entire grid is t.

# You may swim either horizontally or vertically in the grid between two adjacent squares 
# if the original elevation of both squares is less than or equal to the water level at time t.

# Starting from the top left square (0, 0), 
# return the minimum amount of time it will take until it is possible to reach the bottom right square (n - 1, n - 1).

# Example 1:
# Input: grid = [[0,1],[2,3]]
# Output: 3
# Explanation: For a path to exist to the bottom right square grid[1][1] the water elevation must be at least 3. At time t = 3, the water level is 3.

# Example 2:
# Input: grid = [
#   [0,1,2,10],
#   [9,14,4,13],
#   [12,3,8,15],
#   [11,5,7,6]]
# ]
# Output: 8
# Explanation: The water level must be at least 8 to reach the bottom right square. The path is [0, 1, 2, 4, 8, 7, 6].


#solution using dijkstra's algorithm
#time complexity: O(N^2 log N)
#space complexity: O(N^2)

#since we're just iterating through a 2d array, don't need an adjacency list
#we're basically looking for the path that has the lowest possible high value in it
# so 0, 1, 2, 1, the highest value is a 2, since walking doesn't take time

#initialize N as the length of the grid
#initialize a visit set
#initialize a min heap with the first element as the starting point
#the min heap will take (time / max-height, r, c)
#initialize the directions as a list of possible moves
#add the starting point to the visit set

#while the min heap is not empty
#pop the first element, returning the time, row, and column
#check if the current row and column is the last element
# if so, return the time
#loop through the directions
#calculate the new row and column
#check if the new row and column are out of bounds or if they are already in the visit set
# if so, continue
#add the new row and column to the visit set
#push the new row and column to the min heap with the max of the current time and the grid value at the new row and column


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minHeap = [[grid[0][0], 0, 0]] #(time / max-height, r, c)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visit.add((0, 0))
        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == N - 1 and c == N - 1:
                return t
            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if (neiR < 0 or neiC < 0 or
                    neiR == N or neiC == N or
                    (neiR, neiC) in visit):
                        continue
                visit.add((neiR, neiC))
                heapq.heappush(minHeap, [max(t, grid[neiR][neiC]), neiR, neiC])
        
        
       

