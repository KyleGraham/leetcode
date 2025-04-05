# You are given a rectangular island heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
# The islands borders the Pacific Ocean from the top and left sides, and borders the Atlantic Ocean from the bottom and right sides.
# Water can flow in four directions (up, down, left, or right) from a cell to a neighboring cell with height equal or lower. 
# Water can also flow into the ocean from cells adjacent to the ocean.

# Find all cells where water can flow from that cell to both the Pacific and Atlantic oceans. 
# Return it as a 2D list where each element is a list [r, c] representing the row and column of the cell. You may return the answer in any order.

# Example 1:
# Input: heights = [
#   [4,2,7,3,4],
#   [7,4,6,4,7],
#   [6,3,5,3,6]
# ]
# Output: [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]

# Example 2:
# Input: heights = [[1],[1]]
# Output: [[0,0],[0,1]]

#anything less than 0,0 is the pacific
#anything more then len(heights) and len(heights[0]) is the atlantic
#basically start from the nodes that can reach the pacific by default
#so (n, 0) and (0, n) (the first col and the first row)
#and check from those nodes, which other nodes can reach the pacific

#Same with the atlantic
#so (len(heights), n) and (n, len(heights[0]))
#then from those nodes, check which nodes can reach the atlantic

#then find collisons, where nodes can reach both the pacific and atlantic

#solution using dfs
# time complexity: O(m * n) where m is number of rows and n is number of cols
# space complexity: O(m * n)

#initialize rows and cols, along with 2 sets. pac and atl
#pac will hold nodes that can get to the pac ocean
#atl will hold nodes that can get to the atlantic ocean

#loop through all the cols
#call the dfs function on the first row and last row

#loop through all the rows
#call the dfs function on the first col and last col

#initialize the result variable to an empty list
#loop through all the rows and cols
#check if the row and col are in both pac and atl
# if so, append the row and col to the result list
# return res


#the dfs function
#check if the row and col are out of bounds or is in visit, the atl/pac set passed in, or if the height is less than the previous height
#heights here are reversed since we're going backwards. Water can flow if the height is less than or equal to the previous height
#so the reverse is, the height must be greater than or equal to the previous height
#if any of these are true, return

#otherwise, add the row and col to the visit set
#then call the dfs function on all 4 directions


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pac = set()
        atl = set()

        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or 
                r < 0 or c < 0 or r == rows or c == cols or 
                heights[r][c] < prevHeight):
                    return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])




        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res